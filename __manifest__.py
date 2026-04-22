{
    'name': 'Project Management Custom',
    'version': '17.0.1.0.0',
    'category': 'Project',
    'summary': 'Custom fields for project tracking',
    'author': 'Alaa Khaled',
    'depends': [
        'project',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/project_task_views.xml',
        'views/hr_employee_views.xml',
        'views/project_views.xml',
        'views/project_collaborator_views.xml',
    ],
    'installable': True,
    'application': False,
}