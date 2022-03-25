# Copyright 2022 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResUsers(models.Model):

    _inherit = "res.users"

    lims_department_ids = fields.Many2many("lims.department")
