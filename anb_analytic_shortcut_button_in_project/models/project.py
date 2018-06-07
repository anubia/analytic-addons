# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


class ProjectProject(models.Model):
    _inherit = 'project.project'

    @api.multi
    @api.depends('analytic_account_id')
    def _compute_analytic_account_id_count(self):
        for project in self:
            project.analytic_account_id_count = len(
                project.analytic_account_id)

    analytic_account_id_count = fields.Integer(
        compute='_compute_analytic_account_id_count',
        string='Analytic Accounts',
    )

    @api.multi
    def open_analytic_account(self):
        self.ensure_one()
        action = self.env.ref('analytic.action_account_analytic_account_form')
        action_dict = action.read()[0]
        action_dict.update({
            'view_mode': 'form',
            'views': [(False, 'form')],
            'res_id': self.analytic_account_id.id
            if self.analytic_account_id else False,
        })
        return action_dict
