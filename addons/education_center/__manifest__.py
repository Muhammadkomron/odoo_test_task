{
    'name': 'Educational Center Management System',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage students, courses, and enrollments',
    'depends': ['base'],
    'data': [
        'security/education_center_security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student.xml',
        'views/teacher.xml',
        'views/course.xml',
        'views/group.xml',
        'views/income.xml',
        'views/income_dashboard.xml',
        'views/outcome.xml',
        'views/outcome_dashboard.xml',
        'views/weekday.xml',
    ],
    'installable': True,
    'application': True,
}
