# -*- coding: utf-8 -*-

{
    'name': 'exampl-module',
    'summary': """ Odoo Example module """,
    'description': """
        This is an example Odoo module that will be used throughtout the course.
    """,
    'author': 'Ricardo Marin',
    'version': '0.11',
    'license': 'GPL-2',
    'data': [
        'security/example_groups.xml',
        'security/ir.model.access.csv',
        'views/example_menuitems.xml',
        'views/crewmate_views.xml',
        'views/mission_views.xml'
    ],
    'demo': [
        'demo/example_demo.xml'
    ],
    'depends': ['base']
}