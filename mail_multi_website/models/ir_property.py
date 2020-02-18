# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).
from odoo import api, models


class IrProperty(models.Model):
    _inherit = "ir.property"

    @api.multi
    def write(self, vals):
        res = super(IrProperty, self).write(vals)
        field_object_list = [
            self.env.ref("base.field_res_users_email"),
            self.env.ref("mail.field_mail_template_body_html"),
            self.env.ref("mail.field_mail_template_mail_server_id"),
            self.env.ref("mail.field_mail_template_report_template"),
        ]
        for fobj in field_object_list:
            self._update_db_value_website_dependent(fobj)
        return res
