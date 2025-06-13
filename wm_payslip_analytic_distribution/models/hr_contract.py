# -*- coding: utf-8 -*-
# License OPL-1

from odoo import models, fields, api


class HrContract(models.Model):
    _inherit = ["hr.contract", 'analytic.mixin']
    _name = "hr.contract"

    analytic_distribution = fields.Json('Analytic Distribution', copy=True)