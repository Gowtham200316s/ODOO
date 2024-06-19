from odoo import api, fields, models


class Lostreason(models.Model):
    _name = 'lost.reason'
    _description = 'Lost details'
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string="Name"
    )