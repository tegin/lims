# Copyright 2022 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LimsDepartment(models.Model):

    _name = "lims.department"
    _description = "Department"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    user_ids = fields.Many2many("res.users")
