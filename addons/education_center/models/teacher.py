from odoo import models, fields, api


class Teacher(models.Model):
    _name = 'education.teacher'
    _description = 'Teacher'
    _rec_name = 'full_name'

    TEACHER_GENDER = [('male', 'Male'), ('female', 'Female')]

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    phone_number = fields.Char(string='Phone Number', required=True)
    email = fields.Char(string='Email')
    gender = fields.Selection(TEACHER_GENDER, string='Gender')
    age = fields.Integer(string='Age')
    groups = fields.One2many('education.group', 'teacher', string='Assigned Groups')
    outcomes = fields.One2many('education.outcome', 'teacher', string='Outcomes')

    full_name = fields.Char(string='Full Name', compute='_compute_full_name')

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for teacher in self:
            teacher.full_name = f"{teacher.first_name or ''} {teacher.last_name or ''}".strip()
