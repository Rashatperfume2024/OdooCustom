# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock Picking Report Enhancement',
    'summary': 'Stock Picking Report Enhancement',
    'description': """Stock Picking Report Enhancement
""",
    'version': '1.0.0',
    'category': 'Inventory',
    'author': 'Waleed Mohsen',
    'license': 'OPL-1',
    'support': 'mohsen.waleed@gmail.com',
    'depends': ['stock'],
    'data': [
        'views/stock_picking_report_view.xml',
        ],
    'installable': True,
}
