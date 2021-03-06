# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License MIT (https://opensource.org/licenses/MIT).

import odoo.tests
from odoo.api import Environment


@odoo.tests.common.at_install(True)
@odoo.tests.common.post_install(True)
class TestUi(odoo.tests.HttpCase):
    def test_01_mail_private(self):
        # needed because tests are run before the module is marked as
        # installed. In js web will only load qweb coming from modules
        # that are returned by the backend in module_boot. Without
        # this you end up with js, css but no qweb.
        cr = self.registry.cursor()
        env = Environment(cr, self.uid, {})
        env["ir.module.module"].search(
            [("name", "=", "mail_private")], limit=1
        ).state = "installed"
        cr.release()

        env = Environment(self.registry.test_cr, self.uid, {})
        partners = env["res.partner"].search([])
        new_follower = env["res.partner"].search(
            [("name", "ilike", "Ja"), ("email", "!=", False)]
        )
        for partner in partners:
            partner.message_subscribe(new_follower.ids, [])

        self.phantom_js(
            "/web",
            "odoo.__DEBUG__.services['web_tour.tour'].run('mail_private_tour', 1000)",
            "odoo.__DEBUG__.services['web_tour.tour'].tours.mail_private_tour.ready",
            login="admin",
            timeout=90,
        )
