# -*- coding: utf-8 -*-
{
    'name': 'Course Detail Description',
    'summary': """Something about the App.""",
    'description': """
App Name
========
Something about the App.
    """,
    'version': '14.0.1.0',
    'author': 'Company Name',
    'website': 'http://www.company.com',
    'category': 'Tools',
    'sequence': 1,
    'depends': [
        'base',
        'web',
        'website_slides',
    ],
    'data': [
        ## Security
        # 'security/ir.model.access.csv',    
        ## View
        'views/slide_channel_view.xml',
        'views/website_slides_course_main_template.xml'
        
    ],
    'qweb': [
        ## Template
        'static/src/xml/*.xml',
    ],
  
    'external_dependencies': {
        'python': [
            'werkzeug',
        ],
    },
    'icon': '/app_name/static/description/icon.png',
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'EUR',
    'license': 'OPL-1',
    'contributors': [
        'Azharul Amin Mulla',
    ],
}
