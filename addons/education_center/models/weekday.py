from odoo import models, fields


class Weekday(models.Model):
    _name = 'education.weekday'
    _description = 'Weekday'

    DAYS_OF_WEEK = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]

    name = fields.Selection(DAYS_OF_WEEK, string='Weekday', required=True)
