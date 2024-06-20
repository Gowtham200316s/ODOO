# -*- coding: utf-8 -*-
{
    'name': "QR Code of Product Details",
    'summary': "Qr Code",
    'description': """
       Scan the Qr code and get the Product Details
    """,
    'author': "Girik Adhvik",
    'website': "",
    'category': 'Product',
    'version': '13.0',
    'license': 'LGPL-3',
    'images': ['images/QRcode.png'],
    'depends': ['base','product'],
    'data': [
        'views/product_template.xml',
        'reports/product_template_qr_code.xml',
    ],
    "external_dependencies": {"python": ['qrcode'], "bin": []},
    'application': True,
}
