from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    hs_remarks = fields.Char(string="Remarks")

    @api.model_create_multi
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        if res.order_line:
            for line in res.order_line:
                if line.product_id:
                    total_discount = line.compute_customer_discount(line.order_id.partner_id)
                    if total_discount and total_discount > 0:
                        line.discount = round(total_discount, 2)
                # if res.partner_id.tax_reg == 'no':
                #     other_tax = self.env['account.tax'].search([('amount', '=', 4)])
                #     if other_tax:
                #         line.tax_id |= other_tax
        return res

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        for rec in self:
            if rec.order_line:
                for line in rec.order_line:
                    if line.product_id:
                        total_discount = line.compute_customer_discount(line.order_id.partner_id)
                        if total_discount and total_discount > 0:
                            line.discount = round(total_discount, 2)
                    # if rec.partner_id.tax_reg == 'no':
                    #     other_tax = self.env['account.tax'].search([('amount', '=', 4)])
                    #     if other_tax:
                    #         line.tax_id |= other_tax
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    hs_discount = fields.Char(string="Disc %", store=True)

    @api.onchange('product_id', 'product_uom_qty', 'product_packaging_id', 'price_unit')
    def compute_prices(self):
        for rec in self:
            if rec.product_id:
                total_discount = rec.compute_customer_discount(rec.order_id.partner_id)
                if total_discount and total_discount > 0:
                    rec.price_subtotal = 100
                    rec.discount = round(total_discount, 2)

                # if rec.order_id.partner_id.tax_reg == 'no':
                #     other_tax = self.env['account.tax'].search([('amount', '=', 4)])
                #     if other_tax:
                #         rec.tax_id |= other_tax
    def compute_customer_discount(self, customer):
        if customer:
            total_disc = customer.hs_discount + customer.hs_cash_discount + customer.hs_other_discount
            return total_disc
