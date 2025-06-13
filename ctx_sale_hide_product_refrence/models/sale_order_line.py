# -*- coding: utf-8 -*-
from logging import info

from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('product_id')
    def _compute_name(self):
        rec = super(SaleOrderLine, self)._compute_name()
        for line in self:
            if line.name and line.product_id and line.product_id.default_code:
                name = line.name.replace("["+line.product_id.default_code+"] ", "")
                line.name=name
        return rec
