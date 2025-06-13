# -*- coding: utf-8 -*-
# Copyright 2020 CorTex IT Solutions Ltd. (<https://cortexsolutions.net/>)
# License OPL-1

from odoo import models, fields, _, api


class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'

    show_affected_partner = fields.Boolean(string='Add Partner to Journal Item')
