from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    github_account = fields.Char(string='GitHub Account')