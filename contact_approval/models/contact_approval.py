from odoo import models, fields, _
from odoo.exceptions import UserError


class ContactApproval(models.Model):
    _name = "contact.approval"
    _description = "Contact Approval Property"

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("approve", "Approve"),
            ("cancel", "Cancel")
        ],
        string="State",
        default="draft"
    )

    approver_id = fields.Many2one('res.users', string='Approved By')

#========================== Function====================================

    def action_approve(self):
        for rec in self:
            if rec.state == "approve":
                raise UserError(_("Propery set as sold, can't be cancelled"))
            rec.state = "sold"


    def action_cancel(self):
        for rec in self:
            if rec.state == "cancel":
                raise UserError(_("Property set as cancel, can't be sold"))
            rec.state = "cancel"