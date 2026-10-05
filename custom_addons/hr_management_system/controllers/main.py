# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home


class HrmsPortal(http.Controller):
    """Public frontend pages for Metaviz HR Suite.

    Naya page add karne ka tareeqa:
      1. views/ me naya template banao (signup_templates.xml jaisa)
      2. Yahan uska naya route add karo (copy signup)
    """

    # ---- CREATE ACCOUNT ----  URL: http://localhost:8069/signup
    @http.route(['/signup', '/create-account'], type='http', auth='public', website=False)
    def signup(self, **kwargs):
        return request.render('hr_management_system.signup_page')

    # ---- SIGN IN ----  URL: http://localhost:8069/login
    @http.route(['/login', '/signin'], type='http', auth='public', website=False)
    def login(self, **kwargs):
        return request.render('hr_management_system.login_page')

    # ---- DUMMY LOGIN ----  forms yahan POST karte hain
    # csrf=False => CSRF token ki zaroorat nahi (static design).
    # Koi real auth nahi; bas dashboard pe redirect.
    @http.route('/dummy-login', type='http', auth='public', csrf=False, website=False)
    def dummy_login(self, **kwargs):
        return request.redirect('/dashboard')

    # ---- HR DASHBOARD ----  URL: http://localhost:8069/dashboard
    @http.route('/dashboard', type='http', auth='public', website=False)
    def dashboard(self, **kwargs):
        return request.render('hr_management_system.dashboard_page')

    # ---- REQUESTS ----  URL: http://localhost:8069/requests
    @http.route('/requests', type='http', auth='public', website=False)
    def requests(self, **kwargs):
        return request.render('hr_management_system.requests_page')

    # ---- PAYROLL ----  URL: http://localhost:8069/payroll
    @http.route('/payroll', type='http', auth='public', website=False)
    def payroll(self, **kwargs):
        return request.render('hr_management_system.payroll_page')

    # ---- NEW REQUEST ----  URL: http://localhost:8069/requests/new
    @http.route(['/requests/new', '/new-request'], type='http', auth='public', website=False)
    def new_request(self, **kwargs):
        return request.render('hr_management_system.new_request_page')

    # ---- LEAVE list ----  URL: http://localhost:8069/requests/leave
    @http.route('/requests/leave', type='http', auth='public', website=False)
    def requests_leave(self, **kwargs):
        return request.render('hr_management_system.leave_page')

    # ---- EXPENSE REQUEST ----  URL: http://localhost:8069/requests/expense
    @http.route('/requests/expense', type='http', auth='public', website=False)
    def requests_expense(self, **kwargs):
        return request.render('hr_management_system.expense_page')

    # ---- EMPLOY ACTION SHEET ----  URL: http://localhost:8069/requests/employ-action
    @http.route('/requests/employ-action', type='http', auth='public', website=False)
    def requests_employ_action(self, **kwargs):
        return request.render('hr_management_system.employ_action_sheet_page')

    # ---- FUNDS REQUEST ----  URL: http://localhost:8069/requests/funds
    @http.route('/requests/funds', type='http', auth='public', website=False)
    def requests_funds(self, **kwargs):
        return request.render('hr_management_system.funds_page')

    # ---- EMPLOYEE ACTION ----  URL: http://localhost:8069/employee-action
    @http.route(['/employee-action', '/employees/new-action'], type='http', auth='public', website=False)
    def employee_action(self, **kwargs):
        return request.render('hr_management_system.employee_action_page')

    # ---- ATTENDANCE ----  URL: http://localhost:8069/attendance
    @http.route('/attendance', type='http', auth='public', website=False)
    def attendance(self, **kwargs):
        letters = ['F', 'S', 'S', 'M', 'T', 'W', 'T', 'F', 'S', 'S', 'M', 'T', 'W', 'T', 'F',
                   'S', 'S', 'M', 'T', 'W', 'T', 'F', 'S', 'S', 'M', 'T', 'W', 'T', 'F', 'S', 'S']
        weekends = {2, 3, 9, 10, 16, 17, 23, 24, 30, 31}
        days = [{'n': '%02d' % i, 'i': i, 'd': letters[i - 1], 'we': i in weekends}
                for i in range(1, 32)]
        rows = [
            {'id': 'MV-001', 'name': 'Asif Altaf', 'av': 'AA', 'color': '#e0872f',
             'cells': {1: 'public', 4: 'absent', 5: 'public', 8: 'present'}},
            {'id': 'MV-002', 'name': 'Muhammad Asim', 'av': 'MA', 'color': '#2f72c4',
             'cells': {1: 'public', 2: 'public', 5: 'paid', 6: 'paid', 8: 'present'}},
            {'id': 'MV-003', 'name': 'Muhammad Ali', 'av': 'MA', 'color': '#7c5cde',
             'cells': {1: 'public', 2: 'public', 5: 'unpaid', 6: 'hourly', 8: 'present'}},
        ]
        return request.render('hr_management_system.attendance_page', {'days': days, 'rows': rows})

    # ---- ATTENDANCE DETAIL ----  URL: http://localhost:8069/attendance/employee
    @http.route(['/attendance/employee', '/attendance/detail'], type='http', auth='public', website=False)
    def attendance_detail(self, **kwargs):
        def out(n, m):
            return {'n': n, 'sub': m, 'st': 'out'}

        def plain(n):
            return {'n': n, 'st': 'plain'}

        cal = [
            out(26, 'Apr'), out(27, 'Apr'), out(28, 'Apr'), out(29, 'Apr'), out(30, 'Apr'),
            {'n': 1, 'label': 'Labour Day', 'st': 'holiday'},
            {'n': 2, 'label': 'Weekend', 'st': 'weekend'},
            {'n': 3, 'label': 'Weekend', 'st': 'weekend'},
            {'n': 4, 'label': 'Late', 'hrs': '7.3h', 'st': 'late', 'dot': '#f29a2e'},
            {'n': 5, 'label': 'Present', 'hrs': '9.8h', 'st': 'present'},
            {'n': 6, 'label': 'In progress', 'hrs': 'Active', 'st': 'progress'},
            {'n': 7, 'label': 'Annual leave', 'st': 'leave'},
            {'n': 8, 'label': 'Annual leave', 'st': 'leave'},
            plain(9),
            plain(10), plain(11), plain(12), plain(13),
            {'n': 14, 'label': 'Absent', 'st': 'absent'},
            plain(15), plain(16),
            plain(17), plain(18),
            {'n': 19, 'label': 'Unpaid leave', 'st': 'leave'},
            plain(20),
            {'n': 21, 'label': 'Late', 'hrs': '7.6h', 'st': 'late', 'dot': '#f29a2e'},
            plain(22), plain(23),
            plain(24), plain(25),
            {'n': 26, 'label': 'Eid-ul-Adha', 'st': 'holiday'},
            plain(27), plain(28), plain(29), plain(30),
            plain(31),
            out(1, 'Jun'), out(2, 'Jun'), out(3, 'Jun'), out(4, 'Jun'), out(5, 'Jun'), out(6, 'Jun'),
        ]
        return request.render('hr_management_system.attendance_detail_page', {'cal': cal})

    # ---- COMING SOON ----  baaki sab nav items
    # Ek hi route multiple paths handle karta hai; title path se banta hai.
    _COMING_SOON = {
        'employees': 'Employees',
        'performance': 'Performance',
        'recruitment': 'Recruitment',
        'notifications': 'Emails / Notifications',
        'reports': 'Reports',
    }

    @http.route(
        ['/employees',
         '/performance', '/recruitment', '/notifications', '/reports'],
        type='http', auth='public', website=False,
    )
    def coming_soon(self, **kwargs):
        key = request.httprequest.path.strip('/')
        return request.render('hr_management_system.coming_soon', {
            'active': key,
            'page_name': self._COMING_SOON.get(key, 'Coming Soon'),
        })


class HrmsHome(Home):
    """Root '/' ko hamari custom login pe bhejo (Odoo backend login nahi).
    Odoo backend phir bhi /odoo ya /web pe available rahega.
    """

    @http.route('/', type='http', auth='none', website=False)
    def index(self, s_action=None, db=None, **kw):
        return request.redirect('/login')
