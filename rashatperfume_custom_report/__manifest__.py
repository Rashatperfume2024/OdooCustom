{
    'name': "Rashat perfume Custom Reports",
    'author': 'Waleed Mohsen',
    'category': 'Accounting',
    'summary': """Rashat perfume Custom Reports""",
    'license': 'OPL-1',
    'description': """
     Rashat perfume Custom Reports
     """,
    'version': '1.0.1',
    'depends': ['l10n_sa','account','sale'],
    'data': [
        'views/invoice_report.xml',
        'views/payment_receipt_views.xml',
        'views/sale_report.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
