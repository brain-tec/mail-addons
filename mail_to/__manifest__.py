# Copyright 2016 x620 <https://github.com/x620>
# Copyright 2016,2020 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2018 Ruslan Ronzhin
# Copyright 2019 Artem Rafailov <https://it-projects.info/team/Ommo73/>
# Copyright 2020 Denis Mudarisov <https://github.com/trojikman>
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": """Show message recipients""",
    "summary": """Allows you be sure, that all discussion participants were notified""",
    "category": "Discuss",
    "images": ["images/1.png"],
    "version": "11.0.1.1.2",
    "author": "IT-Projects LLC, Pavel Romanchenko",
    "support": "apps@itpp.dev",
    "website": "https://it-projects.info",
    "license": "Other OSI approved licence",  # MIT
    "price": 40.00,
    "currency": "EUR",
    "depends": ["mail_base"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["templates.xml"],
    "qweb": ["static/src/xml/recipient.xml"],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
