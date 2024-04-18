from odoo import models, fields


class HsDistributor(models.Model):
    _name = 'hs.distributor'
    _description = "Hs Distributor"

    name = fields.Char(string="Name")
