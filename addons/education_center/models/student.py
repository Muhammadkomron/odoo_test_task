from odoo import models, fields, api


class Student(models.Model):
    _name = 'education.student'
    _description = 'Student'
    _rec_name = 'full_name'

    STUDENT_GENDER = [('male', 'Male'), ('female', 'Female')]

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    phone_number = fields.Char(string='Phone Number', required=True)
    email = fields.Char(string='Email')
    gender = fields.Selection(STUDENT_GENDER, string='Gender')
    age = fields.Integer(string='Age')
    groups = fields.Many2many('education.group', string='Enrolled Groups')
    incomes = fields.One2many('education.income', 'student', string='Incomes')

    full_name = fields.Char(string='Full Name', compute='_compute_full_name')

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for student in self:
            student.full_name = f"{student.first_name or ''} {student.last_name or ''}".strip()
