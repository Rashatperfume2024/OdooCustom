# -*- coding: utf-8 -*-
# License OPL-1

from odoo import models, fields, api


class HrSalaryRule(models.Model):
    _inherit = ["hr.salary.rule", 'analytic.mixin']
    _name = "hr.salary.rule"

    analytic_distribution = fields.Json('Analytic Distribution', copy=True)