# HR Management System (Metaviz HR Suite)

Frontend module that renders Figma designs as **pixel-perfect, standalone** pages.

## Architecture
- **QWeb** templates for HTML structure (`views/`)
- **SCSS** compiled via a dedicated Odoo asset bundle `hr_management_system.assets_hrms`
  (no Bootstrap / Odoo base CSS → true pixel-perfect)
- **Vanilla JS** for small interactions (OWL only added where a page truly needs it)

## Folder structure
```
hr_management_system/
├── __manifest__.py
├── controllers/
│   └── main.py                 # URL routes
├── views/
│   ├── layout_templates.xml    # reusable clean <html> layout
│   └── signup_templates.xml    # /signup page
└── static/src/
    ├── scss/
    │   ├── _variables.scss      # design tokens (colors, radius, fonts)
    │   ├── _base.scss           # reset + base elements
    │   └── signup.scss          # signup page styles
    ├── js/
    │   └── signup.js            # password toggle + strength + submit guard
    └── img/                     # logos / images
```

## Pages
| URL        | Screen              |
|------------|---------------------|
| `/signup`  | Create your account |

## Run / update
```
D:\odoo1\odoo\venv\Scripts\python.exe D:\odoo1\odoo\odoo-bin -c D:\odoo1\odoo\odoo.conf -d hayat -u hr_management_system
```
