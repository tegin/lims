# Copyright 2022 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):

    _inherit = "product.template"

    laboratory_ok = fields.Boolean(string="Can be used on Lab")
    laboratory_uom_id = fields.Many2one("uom.uom")
