# -*- coding: utf-8 -*-
{
    'name': "srt_wilayah",

    'summary': """
        Indonesia Region data information """,

    'description': """
        Indonesia Region data information, packed in one simple module and can be reused
    """,

    'author': "Sarotama Solusi Integra",
    'website': "http://www.sarotama.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/srt_wilayah.region.csv',
        'data/srt_wilayah.village.csv',
        'data/srt_wilayah.district.csv',
        'data/srt_wilayah.province.csv',
        'views/province.xml',
        'views/region.xml',
        'views/district.xml',
        'views/village.xml',
        'views/menu.xml',
    ],
}