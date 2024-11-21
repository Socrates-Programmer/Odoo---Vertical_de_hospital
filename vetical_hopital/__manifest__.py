# -*- coding: utf-8 -*-
{
    'name': "Vetical de hospital",

    'summary': "El módulo Hospital Vertical está diseñado para facilitar la gestión hospitalaria, administracion de pacientes, creacion de historial medico y generacion de reportes.",

    'description': """
        Application for hospital management
    """,

    'author': "Marcos A",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Healthcare Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/sequences.xml',
        'data/hospital_treatment_data.xml',
    ],
    'installable': True,
    'application': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

