from odoo import models, api, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    retailed_price = fields.Float(string="Retailed Price")
    hs_code = fields.Char(string="HS Code")
