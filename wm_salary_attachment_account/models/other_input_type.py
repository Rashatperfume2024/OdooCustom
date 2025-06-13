# -*- coding: utf-8 -*-
# Copyright 2020 CorTex IT Solutions Ltd. (<https://cortexsolutions.net/>)
# License OPL-1

from odoo import models, fields, _, api

class HrPayslipInputType(models.Model):
    _inherit = 'hr.payslip.input.type'

    create_journal_entry = fields.Boolean('Create Journal Entry')
    debit_account_id = fields.Many2one('account.account', string="Debit Account")
    credit_account_id = fields.Many2one('account.account', string="Credit Account")
    attachment_journal_id = fields.Many2one('account.journal', domain=[('type', '=', 'general')], string="Journal")

    @api.onchange('create_journal_entry')
    def _onchange_create_journal_entry(self):
        self.debit_account_id = False
        self.credit_account_id = False
        self.attachment_journal_id = False

    @api.onchange('available_in_attachments')
    def _onchange_available_in_attachments(self):
        self.create_journal_entry = False
        self.debit_account_id = False
        self.credit_account_id = False
        self.attachment_journal_id = False