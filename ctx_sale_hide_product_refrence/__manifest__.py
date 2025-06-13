# -*- coding: utf-8 -*-
###################################################################################
#    A part of CorTex IT Solutions Modules <https://www.cortexsolutions.net>
#
#    CorTex IT Solutions Ltd.
#    Copyright (C) 2019-TODAY CorTex IT Solutions Ltd (<https://www.cortexsolutions.net>).
#    Author: Waleed Mohsen (<https://www.cortexsolutions.net>)
#
# This program is copyright property of the company mentioned above.
# You can`t redistribute it and/or modify it.
###################################################################################
{
    'name': "Hide Reference",

    'summary': """
        Hide Reference From report of the quotation and replace it with the product name
        """,

    'description': """
     
    """,
    "license": "OPL-1",
    'author': "CorTex IT Solutions Ltd.",
    'website': "http://www.cortexsolutions.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'version': '1.0.0',
    # 'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'report/ir_actions_report_templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #  'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
