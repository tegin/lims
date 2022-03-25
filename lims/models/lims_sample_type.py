# Copyright 2022 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LimsSampleType(models.Model):
    _name = "lims.sample.type"
    _description = "Sample Type"

    name = fields.Char()
    description = fields.Text()
    hazardous = fields.Boolean()
    active = fields.Boolean(default=True)
