from odoo import models, api, fields

class ProjectCollaborator (models.Model):
    _name = 'project.collaborator'
    _description = "Project Collaborator"

    employee = fields.Many2one('hr.employee', string="Employee")
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], required=True)
    employee_id = fields.Many2one('hr.employee', string="Employee")
    project_id = fields.Many2one('project.project', string="Project")

    def action_activate(self):
        for rec in self:
            rec.status = 'active'

    def action_deactivate(self):
        for rec in self:
            rec.status = 'inactive'







