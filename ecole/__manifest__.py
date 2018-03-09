# -*- coding: utf-8 -*-
{
    'name': "ecole",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in
    # modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '10.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/ecole.xml',
        'report/report_cours.xml',
        'report/report_cours_templates.xml',
        'report/report_section.xml',
        'report/report_section_template.xml',
        'report/report_prof.xml',
        'report/report_prof_template.xml',
        'report/report_eleve.xml',
        'report/report_eleve_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
}
