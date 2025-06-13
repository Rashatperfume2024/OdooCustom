# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict
from markupsafe import Markup

from odoo import fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero, plaintext2html


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def _prepare_line_values(self, line, account_id, date, debit, credit):
        result = super()._prepare_line_values(line, account_id, date, debit, credit)
        result['analytic_distribution']= line.salary_rule_id.analytic_distribution or line.slip_id.contract_id.analytic_distribution or False
        return result


    def _get_existing_lines(self, line_ids, line, account_id, debit, credit):
        existing_lines = (
            line_id for line_id in line_ids if
            line_id['name'] == (line.name if line.salary_rule_id.split_move_lines else line.salary_rule_id.name)
            and line_id['account_id'] == account_id
            and ((line_id['debit'] > 0 and credit <= 0) or (line_id['credit'] > 0 and debit <= 0))
            and (
                    (
                        not line_id['analytic_distribution'] and
                        not line.salary_rule_id.analytic_distribution and
                        not line.slip_id.contract_id.analytic_distribution
                    )
                    or line_id['analytic_distribution'] and line.salary_rule_id.analytic_distribution == line_id['analytic_distribution']
                    or line_id['analytic_distribution'] and line.slip_id.contract_id.analytic_distribution == line_id['analytic_distribution']

                )
            and self._check_debit_credit_tags(line_id, line, account_id)
        )
        return existing_lines
