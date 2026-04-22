from odoo import models, api, fields

class Project (models.Model):
    _inherit = "project.project"

    odoo_version = fields.Integer(string="Odoo version")
    odoo_type = fields.Selection([
        ('community','Community'),
        ('enterprise','Enterprise')
    ],default='enterprise')

    repo_name=fields.Char(string="Repository Name")
    repo_url=fields.Char(string="Repository Url")
    hosting = fields.Selection([
        ('on_prem', 'On Prem'),
        ('cloud', 'Cloud Hosting'),
        ('sh', 'Odoo SH'),
        ('online', 'Odoo Online')
    ], string="Hosting")

    hosting_description = fields.Text(string="Hosting Description")
    collaborator_ids = fields.One2many('project.collaborator', 'project_id')
