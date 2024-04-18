from odoo import fields, api, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'


    @api.onchange('product_qty', 'product_packaging_id', 'price_unit')
    def get_line_names(self):
        if self.product_id:
            # todo python connectino with oracle
                # username = 'ERP'
                # password = 'HSG'
                # ip_add = '203.130.21.162'
                # port = '1521'
                # SID = 'orcl19'
                # dsn = cx_Oracle.makedsn(ip_add, port, service_name=SID)
                # try:
                #     connection = cx_Oracle.connect(username, password, dsn)
                # except cx_Oracle.DatabaseError as e:
                #     error, = e.args
                #     print("Database error:", error.message)

            #     todo cridentials of client
            #      user = "ACCT"
            #                 password = "ACCT"
            #                 host = "124.29.223.6"
            #                 port  = '1521'
            #                 sid = 'orcl'
            #                 dsn = cx_Oracle.makedsn(host,port, service_name=sid)
            #                 if dsn:
            #                     try:
            #                         conn = cx_Oracle.connect(user, password, dsn)
            #                     except error:
            #                         print(error)


            # todo this is main code for purchase order
            variant = self.product_id.product_template_attribute_value_ids._get_combination_name()
            name = variant and "%s (%s)" % (self.product_id.name, variant) or self.product_id.name
            self.name = name

