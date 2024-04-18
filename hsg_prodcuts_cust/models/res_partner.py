from odoo import models, api, fields, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    tax_reg = fields.Selection([('yes', 'Yes'),('no', 'No')], default='no', string="Tax Registered")
    cnic = fields.Char(string='CNIC')
    hs_discount = fields.Float(string="Discount")
    hs_cash_discount = fields.Float(string="Cash Discount")
    hs_other_discount = fields.Float(string="Other Discount")
    # party_id = fields.Char(string='Party Id', required=True)
    area_sale_manager = fields.Many2one('hr.employee', string="A S M", help="Area Sales Manager")
    region_sale_manager = fields.Many2one('hr.employee', string="R S M", help="Region Sales Manager")
    national_sale_manager = fields.Many2one('hr.employee', string="N S M", help="National Sales Manager")
    sale_coordinator = fields.Many2one('hr.employee', string="S C", help="Sales Coordinator")
    market_id = fields.Many2one('hs.market', string="Market")
    region_id = fields.Many2one('hs.region', string="Region")
    distributor_id = fields.Many2one('hs.distributor', string="Distributor")

    def write(self, vals):
        if 'cnic' in vals:
            cnic = vals.get('cnic')
            if cnic and (not cnic.isdigit() or len(cnic) != 15 or cnic[5] != '-' or cnic[13] != '-'):
                cnic_digits = ''.join(filter(str.isdigit, cnic))
                if len(cnic_digits) != 13:
                    raise ValidationError("CNIC number must be exactly 13 digits long.")
                formatted_cnic = '-'.join([cnic_digits[:5], cnic_digits[5:12], cnic_digits[12]])
                vals['cnic'] = formatted_cnic
        return super(ResPartner, self).write(vals)