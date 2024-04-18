# -*- coding: utf-8 -*-
{
    'name': "HSG Product And Customer Customization",

    'summary': "This module add some custom fields on customer form and product form(tax,dicount fields and price fields)",

    'description': """
This module add some custom fields on customer form and product form(tax,dicount fields and price fields)
    """,

    'author': "HSxTech",
    'website': "https://www.hsxtech.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'stock', 'contacts', 'sale_management', 'purchase', 'hr','account','account_external_tax'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'data/res_partner_data.xml',
        'views/product_template.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
    ],
    'application': True,
    'installable': True,
    'auto-install': False,
    # 'assets': {
    #     'web.assets_backend': [
    #         'hsg_prodcuts_cust/static/src/components/tax_totals/tax_totals.xml',
    #         'hsg_prodcuts_cust/static/src/components/tax_totals/tax_totals.js',
    #     ],
    # },

}
