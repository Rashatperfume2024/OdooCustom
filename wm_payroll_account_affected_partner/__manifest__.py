# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Payroll Accounting Affected Partner',
    'summary': 'Payroll Accounting Affected Partner',
    'description': """Payroll Accounting Affected Partner
Show employee partner in payslip journal entry
payslip journal entry partner
employee partner in payslip journal entry
add employee partner in payslip journal entry
""",
    'version': '1.0',
    'category': 'Human Resources/Payroll',
    'author': 'Waleed Mohsen',
    'license': 'OPL-1',
    'currency': 'USD',
    'price': 18,
    'support': 'mohsen.waleed@gmail.com',

    'depends': ['hr_payroll_account'],
    'data': [
             'views/hr_salary_rule.xml',
        ],
    'installable': True,
    'images': ['static/description/main_screenshot.png'],
    "live_test_url": 'https://odoo18.wamodoo.com/web?db=OdooApps',
}
