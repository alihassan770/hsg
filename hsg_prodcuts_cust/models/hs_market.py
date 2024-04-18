from odoo import models, fields


class HsMarket(models.Model):
    _name = 'hs.market'
    _description = "Hs Market"

    name = fields.Char(string="Name")
