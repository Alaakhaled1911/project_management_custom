from odoo import models, api, fields

class Project (models.Model):
    _inherit = "project.task"

    task_number = fields.Char(default='New', readonly=True)

    developer_id = fields.Many2one(
        'hr.employee',
        string="Developer"
    )

    functional_consultant_id = fields.Many2one(
        'hr.employee',
        string="Functional Consultant"
    )

    development_status = fields.Selection([
        ('pending', 'Pending'),
        ('ongoing','Ongoing'),
        ('delivered','Delivered'),
        ('onhold','Onhold'),
        ('cancelled','Cancelled')

    ],default='pending')

    module = fields.Char(string="Module")
    branch = fields.Char(string="Branch")
    release_notes = fields.Text(string="Release Note")
    priority_custom = fields.Selection([
        ('high','High'),
        ('medium','Medium'),
        ('low','Low')
    ],default='high')

    internal_deadline = fields.Date(string="Internal Deadline")

    research_allocated_time = fields.Float(
        string='Research and Solution Design Time')
    development_allocated_time = fields.Float(
        string='Development Time')
    testing_allocated_time = fields.Float(
        string='Testing Time')
    allocated_time = fields.Float(
        string='Total Allocated Time',
        compute='_compute_allocated_time')

    @api.depends('research_allocated_time',
                 'development_allocated_time',
                 'testing_allocated_time')
    def _compute_allocated_time(self):
        for rec in self:
            rec.allocated_time = (
                rec.research_allocated_time +
                rec.development_allocated_time +
                rec.testing_allocated_time
            )



    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for rec in records:
            if rec.task_number == 'New':
                rec.task_number = self.env['ir.sequence'].next_by_code('project.task.number') or 'New'
        return records


