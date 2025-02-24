from odoo import fields, models

class ContactType(models.Model):
    _name = "contact.approval.type"
    _description = "contact approval type"

    name = fields.Char(string="Name")