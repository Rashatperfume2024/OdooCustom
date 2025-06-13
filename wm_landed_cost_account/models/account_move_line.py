# -*- coding: utf-8 -*-

from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def button_create_landed_costs(self):
        """Create a `stock.landed.cost` record associated to the account move of `self`, each
        `stock.landed.costs` lines mirroring the current `account.move.line` of self.
        """
        self.ensure_one()
        landed_costs_lines = self.line_ids.filtered(lambda line: line.is_landed_costs_line)

        landed_costs = self.env['stock.landed.cost'].with_company(self.company_id).create({
            'vendor_bill_id': self.id,
            'cost_lines': [(0, 0, {
                'product_id': l.product_id.id,
                'name': l.product_id.name,
                'account_id': l.with_company(l.company_id).product_id.product_tmpl_id.property_account_expense_id.id or
                              l.product_id.product_tmpl_id.get_product_accounts()['stock_input'].id,
                'price_unit': l.currency_id._convert(l.price_subtotal, l.company_currency_id, l.company_id,
                                                     self.invoice_date or fields.Date.context_today(l)),
                'split_method': l.product_id.split_method_landed_cost or 'equal',
            }) for l in landed_costs_lines],
        })
        action = self.env["ir.actions.actions"]._for_xml_id("stock_landed_costs.action_stock_landed_cost")
        return dict(action, view_mode='form', res_id=landed_costs.id, views=[(False, 'form')])


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.depends('is_landed_costs_line')
    def _compute_account_id(self):
        landed_costs_lines = self.filtered(
            lambda l: l.is_landed_costs_line and l.move_id.company_id.anglo_saxon_accounting)
        for line in landed_costs_lines:
            if line and line.product_id:
                fiscal_position = line.move_id.fiscal_position_id
                line.account_id = (line.with_company(
                    line.company_id).product_id.product_tmpl_id.property_account_expense_id.id or
                                   line.with_company(line.company_id).product_id.product_tmpl_id.get_product_accounts(
                                       fiscal_pos=fiscal_position)['stock_input'])
        super(AccountMoveLine, self - landed_costs_lines)._compute_account_id()
