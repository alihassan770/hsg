from odoo import models, fields


class HsRegion(models.Model):
    _name = 'hs.region'
    _description = "Hs Region"

    name = fields.Char(string="Name")
