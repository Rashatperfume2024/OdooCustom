# -*- coding: utf-8 -*-
# Copyright 2020 CorTex IT Solutions Ltd. (<https://cortexsolutions.net/>)
# License OPL-1

from odoo import models, fields, _, api
from odoo.exceptions import ValidationError

class HrSalaryAttachment(models.Model):
    _inherit = 'hr.salary.attachment'

    debit_account_id = fields.Many2one('account.account', string="Debit Account",
                                       related="other_input_type_id.debit_account_id", store=True,
                                       readonly=True)
    attachment_journal_id = fields.Many2one('account.journal', domain=[('type', '=', 'general')], string="Journal",
                                            related="other_input_type_id.attachment_journal_id", store=True,
                                            readonly=True)
    credit_account_id = fields.Many2one('account.account', string="Credit Account",
                                        related="other_input_type_id.credit_account_id", store=True,
                                        readonly=True)
    account_move_id = fields.Many2one('account.move', string="Journal Entry", copy=False)
    account_move_state = fields.Selection(related='account_move_id.state',string='Journal Entry Status',store=True)
    create_journal_entry = fields.Boolean('Create Journal Entry', related="other_input_type_id.create_journal_entry",
                                          store=True,
                                          readonly=True)

    def action_cancel(self):
        for attachment in self:
            if attachment.account_move_id:
                raise ValidationError(_("This salary attachment already have a journal entry so you can't cancel it."))
        super().action_cancel()

    def action_create_draft_journal(self):
        attachments = self.filtered(
            lambda x: x.other_input_type_id.create_journal_entry and not x.account_move_id and x.state == 'open')
        for attachment in attachments:
            attachment._create_journal_entry()
        return True

    def _create_journal_entry(self):
        if self.create_journal_entry:
            if not self.debit_account_id or not self.attachment_journal_id or not self.credit_account_id:
                raise ValidationError(
                    _("The debit or credit accounts or journal is not set on (%s) Other Input type !" % self.other_input_type_id.name))
            move_dict = {
                'narration': '',
                'ref': self.description,
                'journal_id': self.attachment_journal_id.id,
                'date': self.date_start,
                'move_type': 'entry',
            }
            lines = []
            for employee in self.employee_ids:
                debit_line = {
                    'name': self.description,
                    'partner_id': employee.work_contact_id.id,
                    'account_id': self.debit_account_id.id,
                    'date': self.date_start,
                    'debit': self.total_amount,
                    'credit': 0,
                    'amount_currency': (self.total_amount),
                    'currency_id': self.currency_id.id
                }
                credit_line = {
                    'name': self.description,
                    'partner_id': employee.work_contact_id.id,
                    'account_id': self.credit_account_id.id,
                    'date': self.date_start,
                    'debit': 0,
                    'credit': self.total_amount,
                    'amount_currency': -(self.total_amount),
                    'currency_id': self.currency_id.id
                }
                lines.append((0, 0, debit_line))
                lines.append((0, 0, credit_line))
            move_dict['line_ids'] = lines
            move_id = self.env['account.move'].sudo().with_context(default_move_type='entry').create(move_dict)
            self.account_move_id = move_id.id

    def button_open_journal_entry(self):
        ''' Redirect the user to this payment journal.
        :return:    An action on account.move.
        '''
        self.ensure_one()
        if self.account_move_id:
            action = {
                'type': 'ir.actions.act_window',
                'res_model': 'account.move',
                'name': _("Journal Entry"),
                'view_mode': 'form',
                'context': {'create': False},
                'res_id': self.account_move_id.id,
                'views': [(False, 'form')],
            }
        return action

    def action_done(self):
        self.ensure_one()
        if self.employee_count > 1:
            description = self.description
            self.env['hr.salary.attachment'].create([{
                'employee_ids': [(4, employee.id)],
                'company_id': self.company_id.id,
                'description': self.description,
                'other_input_type_id': self.other_input_type_id.id,
                'monthly_amount': self.monthly_amount,
                'total_amount': self.total_amount,
                'paid_amount': self.paid_amount,
                'date_start': self.date_start,
                'date_end': self.date_end,
                'state': 'open',
                'attachment': self.attachment,
                'attachment_name': self.attachment_name,
                'debit_account_id': self.debit_account_id.id,
                'attachment_journal_id': self.attachment_journal_id.id,
                'credit_account_id': self.credit_account_id.id,
            } for employee in self.employee_ids])
            self.write({'state': 'close'})
            self.unlink()
            return {
                'type': 'ir.actions.act_window',
                'name': _('Salary Attachments'),
                'res_model': 'hr.salary.attachment',
                'view_mode': 'list,form',
                'context': {'search_default_description': description},
            }
        self.write({
            'state': 'close',
            'date_end': fields.Date.today(),
        })

