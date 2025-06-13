# -*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict

from odoo.tools import float_compare, float_is_zero, plaintext2html
from odoo import Command, api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from markupsafe import Markup


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def _prepare_line_values(self, line, account_id, date, debit, credit):
        result = super()._prepare_line_values(line, account_id, date, debit, credit)
        partner = line.partner_id
        if not self.company_id.batch_payroll_move_lines:
            if not self.employee_id.work_contact_id:
                raise ValidationError(
                    _('There is no work contact (partner) linked to employee (%s), please link it to a partner!' % self.employee_id.name))
            if line.code == "NET":
                partner = self.employee_id.work_contact_id
            # if the affected partner is checked in salary rules then assign employee partner
        if line.salary_rule_id.show_affected_partner:
            partner = self.employee_id.work_contact_id
        result['partner_id'] = partner.id
        return result
