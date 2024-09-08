from odoo import models, fields


class Outcome(models.Model):
    _name = 'education.outcome'
    _description = 'Outcome'

    OUTCOME_TYPE = [('cash', 'Cash'), ('click', 'Click'), ('payme', 'PayMe')]

    teacher = fields.Many2one('education.teacher', string='Teacher', required=True)
    amount = fields.Float(string='Outcome Amount', required=True)
    time = fields.Char(string='Outcome Time')
    date = fields.Date(string='Outcome Date', default=fields.Date.today)
    outcome_type = fields.Selection(OUTCOME_TYPE, string='Outcome Type', default='cash')
    notes = fields.Text(string='Outcome Notes')

    teacher_full_name = fields.Char(related='teacher.full_name', string="Teacher's Full Name", store=True)
