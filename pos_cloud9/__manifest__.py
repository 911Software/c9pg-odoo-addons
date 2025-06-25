# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'POS Cloud9',
    'version': '18.0.1.0.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Cloud9 Payment Acquirer Integration',
    'description': 'Accept payments via Cloud9 gateway in Odoo.',
    'author': 'C9PG',
    'website': 'https://c9pg.com',
    'license': 'OPL-1',
    'data': [
        'views/pos_payment_method_views.xml',
        'views/res_config_settings_views.xml',
       
    ],
    'depends': ['point_of_sale'],
    'installable': True,
    'auto_install': True,
    'assets': {
        'point_of_sale.assets': [
            'pos_cloud9/static/src/js/payment_cloud9.js',
            'pos_cloud9/static/src/js/models.js',
            'pos_cloud9/static/src/js/pos_cloud9.js',
         ],
        'web.assets_qweb': [
            'pos_cloud9/static/src/xml/**/*',
        ],
    },
    'license': 'LGPL-3',
}
