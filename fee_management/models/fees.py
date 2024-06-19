from odoo import api, fields, models


class FeeManagement(models.Model):
    _name = 'fee.management'
    _description = 'fee details'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "customer_id"

    name = fields.Char(
        string="Name"
    )

    customer_id = fields.Many2one(comodel_name="res.partner",
                                  string=" Customer Name"
                                  )

    image = fields.Image(string='Image')

    state = fields.Selection([('draft', 'Draft'), ('post', 'Post'),
                              ('done', 'Done'), ('cancel', 'Cancel')],
                             default='draft', string="status")

    cancel_id = fields.Many2one(
        comodel_name='lost.reason',
        string="Reason"

    )
    cancel_person_id = fields.Many2one(
        comodel_name='res.users',
        string='Cancel person', default=lambda self: self.env.user

    )

    cancel_date = fields.Date(

        string='Cancel Date', default=fields.Date.today()
    )




    def button_action(self):
        self.state = 'post'