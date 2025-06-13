# -*- coding: utf-8 -*-

{
    'name': 'Hide Cost Price',
    'summary': """Hide cost price of product for specified users""",
    'version': '2.0.0',
    'description': """Product cost price will be visible only for specified 
    group""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'category': 'Stock',
    'depends': ['base', 'product','stock_account'],
    'license': 'AGPL-3',
    'data': [
        'security/groups_view_cost_price.xml',
        'views/product_product_view.xml',
        'views/product_template_view.xml',
        'views/inventory_report.xml'
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}
