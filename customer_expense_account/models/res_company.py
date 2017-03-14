# -*- coding: utf-8 -*-
# © 2016 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    structure_id = fields.Many2one('expense.structure',
                                   string="Expense Structure")
