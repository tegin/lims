# Copyright 2022 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Lims",
    "summary": """
        Laboratory Information Management System""",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "author": "Creu Blanca,Odoo Community Association (OCA)",
    "website": "https://github.com/tegin/lims",
    "depends": ["product"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "views/menu.xml",
        "views/lims_department.xml",
        "views/lims_sample_type.xml",
        "views/lims_sample.xml",
        "views/lims_analysis.xml",
        "views/product_template.xml",
    ],
    "demo": ["demo/demo.xml"],
}
