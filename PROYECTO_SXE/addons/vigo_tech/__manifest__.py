# -*- coding: utf-8 -*-
{
    'name': "VIGO-TECH SOLUTIONS",

    'summary': "Gestión de componentes Gaming y ensamblaje PC",

    'description': """
            Módulo Proyecto SXE.
            Añade campos técnicos a los productos para gestionar mejor los componentes de PC.
            - Especificaciones de hardware.
            - Integración con Compras, Ventas e Inventario.
    """,
    'author': "Saúl, Sofía, Adrián",
    'website': "https://github.com/saulmnz/PROYECTO_SXE.git",
    'version': '1.0',

    'depends': ['base', 'product', 'stock', 'sale_management', 'purchase', 'mrp'],

    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/report.xml',
    ],

    'installable': True,
    'application': True,
}

