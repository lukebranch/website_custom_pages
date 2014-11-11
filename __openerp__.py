{
    'name': 'Website Restricted Pages',
    'description': 'This module demonstrates a method for adding a page to an Odoo website using a custom module.',
    'category': 'Website',
    'version': '1.0',
    'author': 'Luke Branch',
    'depends': ['website', 'portal'],
    'data': [
        'views/portal_user_pages.xml',
    ],
    'application': True,
}
