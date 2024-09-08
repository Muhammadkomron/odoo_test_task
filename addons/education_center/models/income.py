from odoo import models, fields


class Income(models.Model):
    _name = 'education.income'
    _description = 'Income'

    INCOME_TYPE = [('cash', 'Cash'), ('click', 'Click'), ('payme', 'PayMe')]

    student = fields.Many2one('education.student', string='Student', required=True)
    group = fields.Many2one('education.group', string='Group', required=True)
    amount = fields.Float(string='Income Amount', required=True)
    check = fields.Char(string='Income Check', required=True)
    time = fields.Char(string='Income Time')
    date = fields.Date(string='Income Date', default=fields.Date.today)
    income_type = fields.Selection(INCOME_TYPE, string='Income Type', default='cash')
    notes = fields.Text(string='Income Notes')

    student_full_name = fields.Char(related='student.full_name', string="Student's Full Name", store=True)
