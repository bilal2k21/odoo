# -*- coding: utf-8 -*-
{
    'name': 'HR Management System',
    'version': '1.0.0',
    'summary': 'Metaviz HR Suite — frontend pages (pixel-perfect, from Figma)',
    'description': """
HR Management System (Metaviz HR Suite)
=======================================
Custom frontend module that renders the Figma designs as pixel-perfect,
standalone pages (no Odoo website chrome). Styling is written in SCSS and
served through a dedicated Odoo asset bundle (compiled, minified, cache-busted).

Pages:
  - /signup  ->  "Create your account" screen
    """,
    'author': 'Metaviz',
    'website': 'https://metavizai.com',
    'category': 'Human Resources',
    'depends': ['base', 'web'],
    'data': [
        'views/layout_templates.xml',
        'views/signup_templates.xml',
        'views/login_templates.xml',
        'views/dashboard_templates.xml',
        'views/employee_action_templates.xml',
        'views/attendance_templates.xml',
        'views/attendance_detail_templates.xml',
        'views/requests_templates.xml',
        'views/new_request_templates.xml',
        'views/leave_templates.xml',
        'views/expense_templates.xml',
        'views/employ_action_sheet_templates.xml',
        'views/funds_templates.xml',
        'views/payroll_templates.xml',
    ],
    # Dedicated bundle: sirf hamari CSS/JS (koi Bootstrap/Odoo base CSS nahi)
    # -> 100% pixel-perfect. Order matters: variables + shared pehle.
    # Sirf SCSS bundle me (compile/minify/cache-bust ke liye).
    # JS ko bundle me NAHI rakhte: Odoo use odoo.define() module me wrap kar
    # deta hai jo standalone page pe (bina web.assets_frontend loader) execute
    # nahi hota. JS ko layout me raw <script> se load karte hain (niche dekhein).
    'assets': {
        'hr_management_system.assets_hrms': [
            'hr_management_system/static/src/scss/_variables.scss',
            'hr_management_system/static/src/scss/_base.scss',
            'hr_management_system/static/src/scss/_auth.scss',
            'hr_management_system/static/src/scss/signup.scss',
            'hr_management_system/static/src/scss/login.scss',
            'hr_management_system/static/src/scss/dashboard.scss',
            'hr_management_system/static/src/scss/employee_action.scss',
            'hr_management_system/static/src/scss/attendance.scss',
            'hr_management_system/static/src/scss/attendance_detail.scss',
            'hr_management_system/static/src/scss/requests.scss',
            'hr_management_system/static/src/scss/new_request.scss',
            'hr_management_system/static/src/scss/leave.scss',
            'hr_management_system/static/src/scss/expense.scss',
            'hr_management_system/static/src/scss/employ_action_sheet.scss',
            'hr_management_system/static/src/scss/funds.scss',
            'hr_management_system/static/src/scss/notifications.scss',
            'hr_management_system/static/src/scss/payroll.scss',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
