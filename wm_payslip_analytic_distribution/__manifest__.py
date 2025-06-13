# -*- coding: utf-8 -*-
# License OPL-1

{
    'name': "Payroll Analytic Distribution",
    'summary': """
        Payroll Analytic Distribution
        """,
    'description': """
    This app enable you to set analytic Distribution on salary rules/employee contracts then this app will apply it to generated journal entry
odoo Payroll Analytic Distribution
Payroll Analytic Distribution
odoo employee contract analytic account
employee contract analytic account
Salary rule analytic Distribution
payslip journal entry analytic Distribution
    """,
    'author': 'Waleed Mohsen',
    'support': 'mohsen.waleed@gmail.com',
    'currency': 'USD',
    'price': 20,

    'license': 'OPL-1',
    'category': 'HR',
    'version': '1.0.0',
    'depends': ['hr_payroll_account', 'analytic'],
    # always loaded
    'data': [
        'views/hr_contract_views.xml',
        'views/hr_payslip_rule.xml',
    ],
    'images': ['static/description/main_screenshot.png'],
    "installable": True
}
