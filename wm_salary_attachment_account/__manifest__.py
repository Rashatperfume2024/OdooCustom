# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Salary Attachment Journal Entry',
    'version': '1.0.0',
    'category': 'Human Resource',
    'summary': 'Salary Attachment Journal Entry',
    'description': """
    This app enables you to create journal entry from salary attachment.
    """,
    'license': 'OPL-1',
    'author': 'Waleed Mohsen',
    'support': 'mohsen.waleed@gmail.com',
    'currency': 'USD',
    'price': 55.0,
    'depends': ["hr_payroll_account"],
    'data': [
        'views/other_input_type_views.xml',
        'views/salary_attachment_view.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
}
