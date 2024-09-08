from odoo import models, fields


class Group(models.Model):
    _name = 'education.group'
    _description = 'Group'

    name = fields.Char(string='Group Name', required=True)
    start_time = fields.Char(string='Start Time', required=True)
    end_time = fields.Char(string='End Time', required=True)
    course = fields.Many2one('education.course', string='Course', required=True)
    teacher = fields.Many2one('education.teacher', string='Teacher', required=True)
    students = fields.Many2many('education.student', string='Students')
    incomes = fields.One2many('education.income', 'group', string='Incomes')
    weekdays = fields.Many2many('education.weekday', string='Weekdays')
    price = fields.Float(string='Group Price')

    teacher_full_name = fields.Char(related='teacher.full_name', string="Teacher's Full Name", store=True)
