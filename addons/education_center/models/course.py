from odoo import models, fields


class Course(models.Model):
    _name = 'education.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Course Description')
    groups = fields.One2many('education.group', 'course', string='Groups')
