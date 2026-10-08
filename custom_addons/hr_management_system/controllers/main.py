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

    # ---- SETTINGS → SETUP ----  URL: http://localhost:8069/settings/setup
    @http.route(['/settings/setup', '/settings'], type='http', auth='public', website=False)
    def settings_setup(self, **kwargs):
        return request.render('hr_management_system.setup_page')

    # ---- SETTINGS → COMPANY PROFILE ----  URL: http://localhost:8069/settings/company-profile
    @http.route('/settings/company-profile', type='http', auth='public', website=False)
    def settings_company_profile(self, **kwargs):
        return request.render('hr_management_system.company_profile_page')

    # ---- SETTINGS → EMAIL NOTIFICATION ----  URL: http://localhost:8069/settings/email-notification
    @http.route('/settings/email-notification', type='http', auth='public', website=False)
    def settings_email_notification(self, **kwargs):
        return request.render('hr_management_system.email_notification_page')

    # ---- SETTINGS → WORK LOCATIONS (list) ----  URL: http://localhost:8069/settings/work-locations
    @http.route('/settings/work-locations', type='http', auth='public', website=False)
    def settings_work_locations(self, **kwargs):
        locations = [
            {'name': 'Head Office',          'city': 'Karachi',    'modes': ['Manual', 'QR Code', 'Face']},
            {'name': 'Lahore Regional Office', 'city': 'Lahore',   'modes': ['Manual', 'Check-In']},
            {'name': 'Metaviz HQ',           'city': 'Islamabad',  'modes': ['QR Code', 'Face']},
            {'name': 'Gulberg Branch',       'city': 'Lahore',     'modes': ['Manual']},
            {'name': 'SEO Wing — Block B',   'city': 'Rawalpindi', 'modes': ['Check-In', 'QR Code']},
            {'name': 'SEO Wing — Block A',   'city': 'Rawalpindi', 'modes': ['Manual', 'Check-In']},
            {'name': 'Badami Bagh Warehouse', 'city': 'Lahore',    'modes': ['Face', 'Manual']},
            {'name': 'Graphics Studio',      'city': 'Faisalabad', 'modes': ['Voice', 'Video']},
            {'name': 'Development Center',    'city': 'Multan',     'modes': ['QR Code', 'Manual', 'Face']},
        ]
        return request.render('hr_management_system.work_locations_page', {'locations': locations})

    # ---- SETTINGS → ASSETS (list) ----  URL: http://localhost:8069/settings/assets
    @http.route('/settings/assets', type='http', auth='public', website=False)
    def settings_assets(self, **kwargs):
        assets = [
            {'serial': 'MV-LED-035', 'product': 'HP 21',          'type': 'Laptop',  'holder': 'Muhammad Umair',   'dept': 'HR',           'initials': 'MU', 'av': '#e0872f', 'date': '15/12/2025', 'status': 'Assigned',  'scls': 'green'},
            {'serial': 'MV-LED-036', 'product': 'HP 21',          'type': 'Laptop',  'holder': 'Muhammad Husnain', 'dept': 'Data Science', 'initials': 'MH', 'av': '#0a9e86', 'date': '15/12/2025', 'status': 'Assigned',  'scls': 'green'},
            {'serial': 'MV-LED-037', 'product': 'DELL 21',        'type': 'Laptop',  'holder': 'Muhammad Bilal',   'dept': 'Generals',     'initials': 'MB', 'av': '#7c5cde', 'date': '15/12/2025', 'status': 'Assigned',  'scls': 'green'},
            {'serial': 'MV-LED-038', 'product': 'DELL 22',        'type': 'Laptop',  'holder': 'Muhammad Umair',   'dept': 'HR',           'initials': 'MU', 'av': '#0a7e9b', 'date': '15/12/2025', 'status': 'Assigned',  'scls': 'green'},
            {'serial': 'MV-LED-039', 'product': 'DELL 22',        'type': 'Laptop',  'holder': '',                 'dept': '',             'initials': '',   'av': '',        'date': '15/12/2025', 'status': 'Available', 'scls': 'blue'},
            {'serial': 'MV-MON-066', 'product': 'LG UltraFine 27"', 'type': 'Monitor', 'holder': '',               'dept': '',             'initials': '',   'av': '',        'date': '28/01/2025', 'status': 'Available', 'scls': 'blue'},
            {'serial': 'MV-MOB-839', 'product': 'iPhone 15',      'type': 'Mobile',  'holder': 'Meera Joshi',      'dept': 'Sales',        'initials': 'MJ', 'av': '#e0a22f', 'date': '19/06/2024', 'status': 'Assigned',  'scls': 'green'},
            {'serial': 'MV-LAP-158', 'product': 'ThinkPad X1',    'type': 'Laptop',  'holder': 'Nikhil Verma',     'dept': 'Finance',      'initials': 'NV', 'av': '#2f72c4', 'date': '02/04/2023', 'status': 'Broken',    'scls': 'red'},
            {'serial': 'MV-LAP-097', 'product': 'MacBook Air 13"', 'type': 'Laptop', 'holder': '',                 'dept': '',             'initials': '',   'av': '',        'date': '22/05/2020', 'status': 'Disposed',  'scls': 'slate'},
            {'serial': 'MV-MOB-014', 'product': 'Galaxy S22',     'type': 'Mobile',  'holder': '',                 'dept': '',             'initials': '',   'av': '',        'date': '30/03/2022', 'status': 'Sold',      'scls': 'rose'},
        ]
        return request.render('hr_management_system.assets_page', {'assets': assets})

    # ---- SETTINGS → ROLES & PERMISSIONS ----  URL: http://localhost:8069/settings/roles
    @http.route('/settings/roles', type='http', auth='public', website=False)
    def settings_roles(self, **kwargs):
        roles = [
            {'letter': 'X', 'av': '#e5564b', 'name': 'xyz',       'desc': 'Pre-filled from HR Template', 'users': 0,  'perms': '9 Permissions',  'all_access': False, 'scope': 'Entire Organization'},
            {'letter': 'C', 'av': '#2b3440', 'name': 'CEO',       'desc': 'No description',              'users': 1,  'perms': 'All Access',     'all_access': True,  'scope': 'Entire Organization'},
            {'letter': 'H', 'av': '#16a34a', 'name': 'HR',        'desc': 'No description',              'users': 5,  'perms': '25 Permissions', 'all_access': False, 'scope': 'Team Members'},
            {'letter': 'F', 'av': '#2f72c4', 'name': 'Finance',   'desc': 'No description',              'users': 4,  'perms': '22 Permissions', 'all_access': False, 'scope': 'Department Only'},
            {'letter': 'M', 'av': '#e0872f', 'name': 'Manager',   'desc': 'No description',              'users': 6,  'perms': '18 Permissions', 'all_access': False, 'scope': 'Department Only'},
            {'letter': 'T', 'av': '#0a9e86', 'name': 'Team Lead', 'desc': 'No description',              'users': 8,  'perms': '12 Permissions', 'all_access': False, 'scope': 'Team Members'},
            {'letter': 'E', 'av': '#8a97a0', 'name': 'Employee',  'desc': 'No description',              'users': 25, 'perms': '6 Permissions',  'all_access': False, 'scope': 'Own Data Only'},
        ]
        return request.render('hr_management_system.roles_page', {'roles': roles})

    # ---- SETTINGS → AUDIT LOGS ----  URL: http://localhost:8069/settings/audit
    @http.route('/settings/audit', type='http', auth='public', website=False)
    def settings_audit(self, **kwargs):
        logs = [
            {'date': '07 Oct 2026', 'time': '10:42 AM', 'user': 'Mujahid Ali',       'role': 'HR Manager',        'initials': 'MA', 'av': '#e0872f', 'action': 'Update',  'acls': 'update',  'module': 'Roles & Permissions', 'detail': 'Updated permissions for "HR" role',          'status': 'Success', 'scls': 'success'},
            {'date': '07 Oct 2026', 'time': '09:15 AM', 'user': 'Mujahid Ali',       'role': 'HR Manager',        'initials': 'MA', 'av': '#e0872f', 'action': 'Login',   'acls': 'login',   'module': 'Authentication',      'detail': 'Signed in from Chrome · Lahore, PK',          'status': 'Success', 'scls': 'success'},
            {'date': '06 Oct 2026', 'time': '06:30 PM', 'user': 'Priya Sundaram',    'role': 'HR Specialist',     'initials': 'PS', 'av': '#0a7e9b', 'action': 'Create',  'acls': 'create',  'module': 'Employees',           'detail': 'Added new employee "Marcus Kline"',           'status': 'Success', 'scls': 'success'},
            {'date': '06 Oct 2026', 'time': '04:12 PM', 'user': 'Eleanor Whitfield', 'role': 'VP Engineering',    'initials': 'EW', 'av': '#d4578a', 'action': 'Approve', 'acls': 'approve', 'module': 'Leave',               'detail': 'Approved leave request #LV-2041',             'status': 'Success', 'scls': 'success'},
            {'date': '06 Oct 2026', 'time': '02:58 PM', 'user': 'Marcus Kline',      'role': 'Finance Analyst',   'initials': 'MK', 'av': '#16a34a', 'action': 'Export',  'acls': 'export',  'module': 'Payroll',             'detail': 'Exported payroll report (Sep 2026)',          'status': 'Success', 'scls': 'success'},
            {'date': '06 Oct 2026', 'time': '11:05 AM', 'user': 'Unknown',           'role': '—',                 'initials': '??', 'av': '#8a97a0', 'action': 'Login',   'acls': 'login',   'module': 'Authentication',      'detail': 'Failed login attempt (wrong password)',       'status': 'Failed',  'scls': 'failed'},
            {'date': '05 Oct 2026', 'time': '05:47 PM', 'user': 'Kwame Roux',        'role': 'Customer Success',  'initials': 'KR', 'av': '#c98a1d', 'action': 'Delete',  'acls': 'delete',  'module': 'Assets',              'detail': 'Removed asset "MV-LAP-097"',                  'status': 'Success', 'scls': 'success'},
            {'date': '05 Oct 2026', 'time': '03:21 PM', 'user': 'Leila Moretti',     'role': 'Marketing Lead',    'initials': 'LM', 'av': '#7c5cde', 'action': 'Update',  'acls': 'update',  'module': 'Attendance',          'detail': 'Edited attendance regulation for 3 days',     'status': 'Success', 'scls': 'success'},
            {'date': '05 Oct 2026', 'time': '10:30 AM', 'user': 'Mujahid Ali',       'role': 'HR Manager',        'initials': 'MA', 'av': '#e0872f', 'action': 'Create',  'acls': 'create',  'module': 'Settings',            'detail': 'Created work location "Head Office"',         'status': 'Success', 'scls': 'success'},
            {'date': '04 Oct 2026', 'time': '09:02 AM', 'user': 'Nadir Bao',         'role': 'Product Designer',  'initials': 'NB', 'av': '#2f72c4', 'action': 'Logout',  'acls': 'logout',  'module': 'Authentication',      'detail': 'Signed out',                                  'status': 'Success', 'scls': 'success'},
        ]
        return request.render('hr_management_system.audit_page', {'logs': logs})

    # ---- COMPANY DOCUMENTS ----  URL: http://localhost:8069/documents
    @http.route('/documents', type='http', auth='public', website=False)
    def documents(self, **kwargs):
        docs = [
            {'f': 'pdf', 'nm': 'Remote Work Policy 2026', 'mt': 'PDF · 2.4 MB', 'cat': 'Policies', 'cc': '#2f72c4', 'ty': 'internal', 'tl': 'Internal', 'up': 'Mujahid Ali', 'ua': 'MA', 'uc': '#e0872f', 'dt': '29 Jun 2026', 'st': 'active', 'sl': 'Active'},
            {'f': 'pdf', 'nm': 'AWS Master Service Agreement', 'mt': 'PDF · 5.1 MB', 'cat': 'Contracts', 'cc': '#7c5cde', 'ty': 'external', 'tl': 'External', 'up': 'Bilal Ahmed', 'ua': 'BA', 'uc': '#16a34a', 'dt': '28 Jun 2026', 'st': 'active', 'sl': 'Active'},
            {'f': 'xlsx', 'nm': 'Q2 2026 Payroll Register', 'mt': 'XLSX · 880 KB', 'cat': 'Finance', 'cc': '#16a34a', 'ty': 'internal', 'tl': 'Internal', 'up': 'Bilal Ahmed', 'ua': 'BA', 'uc': '#16a34a', 'dt': '27 Jun 2026', 'st': 'active', 'sl': 'Active'},
            {'f': 'docx', 'nm': 'Employee Handbook v8', 'mt': 'DOCX · 3.7 MB', 'cat': 'HR', 'cc': '#f29a2e', 'ty': 'internal', 'tl': 'Internal', 'up': 'Ayesha Khan', 'ua': 'AK', 'uc': '#2f72c4', 'dt': '26 Jun 2026', 'st': 'draft', 'sl': 'Draft'},
            {'f': 'pdf', 'nm': 'ISO 27001 Certificate', 'mt': 'PDF · 1.2 MB', 'cat': 'IT & Security', 'cc': '#0a7e9b', 'ty': 'external', 'tl': 'External', 'up': 'Usman Tariq', 'ua': 'UT', 'uc': '#7c5cde', 'dt': '24 Jun 2026', 'st': 'expiring', 'sl': 'Expiring'},
            {'f': 'pdf', 'nm': 'Fire Safety Inspection Report', 'mt': 'PDF · 960 KB', 'cat': 'Health & Safety', 'cc': '#e5564b', 'ty': 'external', 'tl': 'External', 'up': 'Hamza Iqbal', 'ua': 'HI', 'uc': '#e5307a', 'dt': '21 Jun 2026', 'st': 'active', 'sl': 'Active'},
        ]
        expiring = [
            {'f': 'pdf', 'nm': 'Office Lease — Lahore HQ', 'mt': 'PDF', 'ed': '09 Jul 2026', 'dr': '10 days', 'dc': 'red'},
            {'f': 'pdf', 'nm': 'Commercial Insurance Policy', 'mt': 'PDF', 'ed': '14 Jul 2026', 'dr': '15 days', 'dc': 'red'},
            {'f': 'pdf', 'nm': 'ISO 27001 Certificate', 'mt': 'PDF', 'ed': '19 Jul 2026', 'dr': '20 days', 'dc': 'orange'},
            {'f': 'docx', 'nm': 'Data Processing Agreement — Stripe', 'mt': 'DOCX', 'ed': '23 Jul 2026', 'dr': '24 days', 'dc': 'orange'},
            {'f': 'pdf', 'nm': 'Vendor NDA — OdoBridge', 'mt': 'PDF', 'ed': '27 Jul 2026', 'dr': '28 days', 'dc': 'green'},
        ]
        return request.render('hr_management_system.documents_page', {'docs': docs, 'expiring': expiring})

    # ---- RECRUITMENT ----  URL: http://localhost:8069/recruitment
    @http.route('/recruitment', type='http', auth='public', website=False)
    def recruitment(self, **kwargs):
        jobs = [
            {'c': 'SBE', 'cc': '#2f72c4', 't': 'Senior Backend Engineer', 'ty': 'Full-time · On-site · Codinative', 'dp': 'Engineering', 'lo': 'Lahore HQ', 'ap': '42', 'mgr': 'EW', 'mc': '#2f72c4', 'st': 'open', 'sl': 'Open'},
            {'c': 'MLE', 'cc': '#0a7e9b', 't': 'ML Engineer', 'ty': 'Full-time · Hybrid · Metaviz AI', 'dp': 'AI Platform', 'lo': 'Remote', 'ap': '38', 'mgr': 'AB', 'mc': '#2b3440', 'st': 'open', 'sl': 'Open'},
            {'c': 'PD', 'cc': '#7c5cde', 't': 'Product Designer', 'ty': 'Full-time · Hybrid · Metaviz AI', 'dp': 'Design', 'lo': 'Karachi', 'ap': '31', 'mgr': 'NB', 'mc': '#2f72c4', 'st': 'open', 'sl': 'Open'},
            {'c': 'FE', 'cc': '#16a34a', 't': 'Frontend Engineer', 'ty': 'Full-time · On-site · Codinative', 'dp': 'Engineering', 'lo': 'Lahore HQ', 'ap': '24', 'mgr': 'EW', 'mc': '#2f72c4', 'st': 'open', 'sl': 'Open'},
            {'c': 'EM', 'cc': '#e0872f', 't': 'Engineering Manager', 'ty': 'Full-time · On-site · Codinative', 'dp': 'Engineering', 'lo': 'Lahore HQ', 'ap': '18', 'mgr': 'SR', 'mc': '#e0872f', 'st': 'open', 'sl': 'Open'},
            {'c': 'AE', 'cc': '#e5564b', 't': 'Account Executive', 'ty': 'Full-time · Hybrid · DevoraHub', 'dp': 'Sales', 'lo': 'Islamabad', 'ap': '27', 'mgr': 'KR', 'mc': '#7c5cde', 'st': 'open', 'sl': 'Open'},
            {'c': 'DO', 'cc': '#0a7e9b', 't': 'DevOps Engineer', 'ty': 'Full-time · Remote · Codinative', 'dp': 'Platform', 'lo': 'Remote', 'ap': '15', 'mgr': 'EW', 'mc': '#2f72c4', 'st': 'paused', 'sl': 'Paused'},
            {'c': 'TW', 'cc': '#8a97a0', 't': 'Technical Writer', 'ty': 'Contract · Remote · OdoBridge', 'dp': 'Product', 'lo': 'Remote', 'ap': False, 'mgr': 'PS', 'mc': '#16a34a', 'st': 'draft', 'sl': 'Draft'},
            {'c': 'HRP', 'cc': '#f29a2e', 't': 'HR Partner', 'ty': 'Full-time · On-site · Metaviz Group', 'dp': 'People', 'lo': 'Lahore HQ', 'ap': False, 'mgr': 'SR', 'mc': '#e0872f', 'st': 'draft', 'sl': 'Draft'},
        ]
        return request.render('hr_management_system.recruitment_page', {'jobs': jobs})

    # ---- RECRUITMENT → CANDIDATES ----  URL: http://localhost:8069/recruitment/candidates
    @http.route('/recruitment/candidates', type='http', auth='public', website=False)
    def recruitment_candidates(self, **kwargs):
        cands = [
            {'av': 'DA', 'ac': '#2f72c4', 'n': 'Daniyal Ahmed', 'src': 'LinkedIn', 'role': 'Senior Backend Engineer', 'co': 'Codinative', 'st': 'interview', 'sl': 'Interview', 'r': 5, 'ago': '6 days ago'},
            {'av': 'AM', 'ac': '#7c5cde', 'n': 'Ahsan Mirza', 'src': 'Career page', 'role': 'ML Engineer', 'co': 'Metaviz AI', 'st': 'interview', 'sl': 'Interview', 'r': 5, 'ago': '4 days ago'},
            {'av': 'BY', 'ac': '#0a7e9b', 'n': 'Bilal Yousafzai', 'src': 'LinkedIn', 'role': 'Senior Backend Engineer', 'co': 'Codinative', 'st': 'offer', 'sl': 'Offer', 'r': 5, 'ago': '9 days ago'},
            {'av': 'AI', 'ac': '#16a34a', 'n': 'Adeel Iqbal', 'src': 'Referral', 'role': 'Engineering Manager', 'co': 'Codinative', 'st': 'offer', 'sl': 'Offer', 'r': 5, 'ago': '12 days ago'},
            {'av': 'IY', 'ac': '#e5564b', 'n': 'Imran Yousuf', 'src': 'Referral', 'role': 'Frontend Engineer', 'co': 'Codinative', 'st': 'interview', 'sl': 'Interview', 'r': 4, 'ago': '7 days ago'},
            {'av': 'HA', 'ac': '#2b3440', 'n': 'Hamza Akram', 'src': 'LinkedIn', 'role': 'Senior Backend Engineer', 'co': 'Codinative', 'st': 'screening', 'sl': 'Screening', 'r': 4, 'ago': '3 days ago'},
            {'av': 'FH', 'ac': '#0a7e9b', 'n': 'Faisal Hayat', 'src': 'Referral', 'role': 'Frontend Engineer', 'co': 'Codinative', 'st': 'screening', 'sl': 'Screening', 'r': 5, 'ago': '4 days ago'},
            {'av': 'WS', 'ac': '#e5307a', 'n': 'Wasif Sohail', 'src': 'Dribbble', 'role': 'Product Designer', 'co': 'Metaviz AI', 'st': 'screening', 'sl': 'Screening', 'r': 3, 'ago': '5 days ago'},
            {'av': 'AT', 'ac': '#2f72c4', 'n': 'Ahmed Tariq', 'src': 'LinkedIn', 'role': 'Senior Backend Engineer', 'co': 'Codinative', 'st': 'applied', 'sl': 'Applied', 'r': 4, 'ago': '1 day ago'},
            {'av': 'SA', 'ac': '#7c5cde', 'n': 'Saif Anwar', 'src': 'Career page', 'role': 'ML Engineer', 'co': 'Metaviz AI', 'st': 'applied', 'sl': 'Applied', 'r': 4, 'ago': '1 day ago'},
            {'av': 'TR', 'ac': '#16a34a', 'n': 'Talha Riaz', 'src': 'Referral', 'role': 'Senior Engineer', 'co': 'Codinative', 'st': 'hired', 'sl': 'Hired', 'r': 5, 'ago': '21 days ago'},
            {'av': 'OB', 'ac': '#e0872f', 'n': 'Owais Bashir', 'src': 'Career page', 'role': 'ML Engineer', 'co': 'Metaviz AI', 'st': 'applied', 'sl': 'Applied', 'r': 4, 'ago': '2 days ago'},
        ]
        return request.render('hr_management_system.candidates_page', {'cands': cands})

    # ---- RECRUITMENT → PIPELINE ----  URL: http://localhost:8069/recruitment/pipeline
    @http.route('/recruitment/pipeline', type='http', auth='public', website=False)
    def recruitment_pipeline(self, **kwargs):
        cols = [
            {'name': 'Applied', 'n': 3, 'dot': '#9ca3af', 'cards': [
                {'nm': 'Rabia Saleem', 'bd': 'REFERRED', 'bt': 'referred', 'role': 'Senior Backend Engineer', 'exp': '6 Years Experience', 'rec': 'Nadia', 'ra': 'NK', 'rc': '#7c5cde'},
                {'nm': 'Ahmed Tariq', 'bd': 'NEW', 'bt': 'new', 'role': 'Senior Backend Engineer', 'exp': '8 Years Experience', 'rec': 'Omar', 'ra': 'OS', 'rc': '#16a34a'},
                {'nm': 'Junaid Khan', 'bd': 'NEW', 'bt': 'new', 'role': 'Senior Backend Engineer', 'exp': '5 Years Experience', 'rec': 'Samira', 'ra': 'SR', 'rc': '#e0872f'},
            ]},
            {'name': 'Screening', 'n': 2, 'dot': '#2f72c4', 'cards': [
                {'nm': 'Hamza Akram', 'bd': 'SHORTLISTED', 'bt': 'short', 'role': 'Senior Backend Engineer', 'exp': '7 Years Experience', 'rec': 'Omar', 'ra': 'OS', 'rc': '#16a34a'},
                {'nm': 'Sana Pervez', 'bd': 'ON HOLD', 'bt': 'hold', 'role': 'Senior Backend Engineer', 'exp': '5 Years Experience', 'rec': 'Nadia', 'ra': 'NK', 'rc': '#7c5cde'},
            ]},
            {'name': 'Initial Interview (HR)', 'n': 1, 'dot': '#2f72c4', 'cards': [
                {'nm': 'Imran Yousuf', 'bd': 'HIGH PRIORITY', 'bt': 'priority', 'role': 'Senior Backend Engineer', 'date': 'HR Interview - 23 Jun 2026', 'exp': '6 Years Experience', 'rec': 'Nadia', 'ra': 'NK', 'rc': '#7c5cde'},
            ]},
            {'name': 'Assessment / Test', 'n': 1, 'dot': '#7c5cde', 'cards': [
                {'nm': 'Kamran Shah', 'bd': 'REFERRED', 'bt': 'referred', 'role': 'Senior Backend Engineer', 'exp': '7 Years Experience', 'rec': 'Omar', 'ra': 'OS', 'rc': '#16a34a'},
            ]},
            {'name': 'Technical Interview', 'n': 2, 'dot': '#f29a2e', 'cards': [
                {'nm': 'Daniyal Ahmed', 'bd': '', 'bt': '', 'role': 'Senior Backend Engineer', 'exp': '6 Years Experience', 'rec': 'Samira', 'ra': 'SR', 'rc': '#e0872f'},
                {'nm': 'Faisal Hayat', 'bd': '', 'bt': '', 'role': 'Senior Backend Engineer', 'exp': '5 Years Experience', 'rec': 'Nadia', 'ra': 'NK', 'rc': '#7c5cde'},
            ]},
            {'name': 'Offer', 'n': 0, 'dot': '#16a34a', 'cards': []},
        ]
        return request.render('hr_management_system.pipeline_page', {'cols': cols})

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

    # ---- EMAILS / NOTIFICATIONS (center) ----  URL: http://localhost:8069/notifications
    @http.route('/notifications', type='http', auth='public', website=False)
    def notifications(self, **kwargs):
        notes = [
            {'type': 'Approval',  'icls': 'green',  'title': 'Your Leave Application Is Approved',       'desc': 'Your leave from 20 Apr to 22 Apr 2026 has been approved by Eleanor Whitfield.', 'time': '2h ago',    'unread': True},
            {'type': 'Approval',  'icls': 'orange', 'title': 'New Leave Request Awaiting Your Approval', 'desc': 'Priya Sundaram applied for 3 days of annual leave (05–07 Oct).',                 'time': '4h ago',    'unread': True},
            {'type': 'Payroll',   'icls': 'purple', 'title': 'September Payslip Is Ready',               'desc': 'Your payslip for September 2026 has been generated and emailed to you.',         'time': 'Today',     'unread': True},
            {'type': 'Document',  'icls': 'teal',   'title': 'Document Expiring Soon',                   'desc': 'Your "Employment Contract" expires in 14 days. Please renew it.',                'time': 'Yesterday', 'unread': True},
            {'type': 'Mention',   'icls': 'blue',   'title': 'Mujahid Ali mentioned you',               'desc': '“@you can you review the Q4 hiring plan before Friday?”',                        'time': 'Yesterday', 'unread': False},
            {'type': 'Employee',  'icls': 'green',  'title': 'New Employee Onboarded',                   'desc': 'Marcus Kline (Finance Analyst) joined the organization today.',                  'time': '2 days ago', 'unread': False},
            {'type': 'Attendance','icls': 'blue',   'title': 'Attendance Regulation Approved',           'desc': 'Your attendance regulation for 28 Apr 2026 has been approved.',                 'time': '3 days ago', 'unread': False},
            {'type': 'System',    'icls': 'gray',   'title': 'Scheduled Maintenance',                    'desc': 'The system will be briefly unavailable on 12 Oct, 1:00–2:00 AM PKT.',           'time': '5 days ago', 'unread': False},
        ]
        return request.render('hr_management_system.notifications_page', {'notes': notes})

    # ---- REPORTS ----  URL: http://localhost:8069/reports
    @http.route('/reports', type='http', auth='public', website=False)
    def reports(self, **kwargs):
        recent = [
            {'name': 'October Attendance Summary', 'type': 'Attendance',  'tcls': 'blue',   'date': '07 Oct 2026', 'size': '1.2 MB'},
            {'name': 'September Payroll Report',    'type': 'Payroll',     'tcls': 'purple', 'date': '01 Oct 2026', 'size': '840 KB'},
            {'name': 'Q3 Leave Report',            'type': 'Leave',       'tcls': 'teal',   'date': '30 Sep 2026', 'size': '512 KB'},
            {'name': 'Employee Directory',         'type': 'Employee',    'tcls': 'green',  'date': '28 Sep 2026', 'size': '2.1 MB'},
            {'name': 'Recruitment Funnel Q3',      'type': 'Recruitment', 'tcls': 'orange', 'date': '25 Sep 2026', 'size': '680 KB'},
            {'name': 'Asset Inventory Report',     'type': 'Asset',       'tcls': 'dark',   'date': '20 Sep 2026', 'size': '430 KB'},
        ]
        return request.render('hr_management_system.reports_page', {'recent': recent})

    # ---- PERFORMANCE ----  URL: http://localhost:8069/performance
    @http.route('/performance', type='http', auth='public', website=False)
    def performance(self, **kwargs):
        goals = [
            {'title': 'Complete Q3 performance reviews', 'pct': 88, 'color': 'green'},
            {'title': 'Reduce attrition to under 8%',     'pct': 72, 'color': 'teal'},
            {'title': 'Improve average eNPS to 45',       'pct': 60, 'color': 'orange'},
            {'title': 'Manager 1:1 coverage',             'pct': 95, 'color': 'blue'},
        ]
        performers = [
            {'name': 'Eleanor Whitfield', 'role': 'VP Engineering',  'initials': 'EW', 'av': '#d4578a', 'score': '4.9'},
            {'name': 'Aarav Hegde',       'role': 'Senior Engineer', 'initials': 'AH', 'av': '#e0872f', 'score': '4.8'},
            {'name': 'Priya Sundaram',    'role': 'HR Specialist',   'initials': 'PS', 'av': '#0a7e9b', 'score': '4.7'},
            {'name': 'Marcus Kline',      'role': 'Finance Analyst', 'initials': 'MK', 'av': '#16a34a', 'score': '4.6'},
        ]
        reviews = [
            {'emp': 'Aarav Hegde',    'initials': 'AH', 'av': '#e0872f', 'role': 'Senior Engineer', 'cycle': 'Q3 2026', 'score': '4.8', 'status': 'Completed',   'scls': 'green'},
            {'emp': 'Nadir Bao',      'initials': 'NB', 'av': '#2f72c4', 'role': 'Product Designer', 'cycle': 'Q3 2026', 'score': '4.2', 'status': 'Completed',   'scls': 'green'},
            {'emp': 'Leila Moretti',  'initials': 'LM', 'av': '#7c5cde', 'role': 'Marketing Lead',   'cycle': 'Q3 2026', 'score': '—',   'status': 'In Progress', 'scls': 'blue'},
            {'emp': 'Tomás Okafor',   'initials': 'TO', 'av': '#e5564b', 'role': 'QA Engineer',      'cycle': 'Q3 2026', 'score': '—',   'status': 'Pending',     'scls': 'orange'},
            {'emp': 'Kwame Roux',     'initials': 'KR', 'av': '#c98a1d', 'role': 'Customer Success', 'cycle': 'Q3 2026', 'score': '3.9', 'status': 'Completed',   'scls': 'green'},
            {'emp': 'Priya Sundaram', 'initials': 'PS', 'av': '#0a7e9b', 'role': 'HR Specialist',    'cycle': 'Q3 2026', 'score': '4.7', 'status': 'Completed',   'scls': 'green'},
        ]
        return request.render('hr_management_system.performance_page', {
            'goals': goals, 'performers': performers, 'reviews': reviews,
        })

    # ---- COMING SOON ----  baaki sab nav items
    # Ek hi route multiple paths handle karta hai; title path se banta hai.
    _COMING_SOON = {
        'employees': 'Employees',
    }

    @http.route(
        ['/employees'],
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
