{
    'name': 'Fee management',
    'author': 'Girik Adhvik ',
    'category': 'Fee',
    'version': '15.0',
    'price': '0.5',
    'currency': 'USD',
    'description': """
This module information about fees""",
    'data': [

        'security/ir.model.access.csv',

        'wizard/lost.xml',

        'views/fee.xml',
        'views/lost_reason.xml',

        'views/menu.xml',

    ],
'depends': [
    'base', 'product'],

    'license': 'LGPL-3',
}
