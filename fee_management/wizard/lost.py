from odoo import models, fields


class lost(models.TransientModel):
    _name = "lost.fee"
    _description = 'Lost Reason'

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

    admit_date = fields.Datetime(
        string="Cancel Date Time",
        index=True, readonly=True,
        default=fields.Datetime.now)

    reason = fields.Html(
        string=""
    )

    def fee_cancel(self):
        self.ensure_one()
        fee = self.env['fee.management'].browse(self.env.context.get('active_ids'))
        fee.cancel_id = self.cancel_id or False
        fee.state = 'cancel'
        return True
