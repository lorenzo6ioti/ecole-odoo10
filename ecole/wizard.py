# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'ecole.wizard'

    def _default_cours(self):
        return self.env['ecole.cours'].browse(self._context.get('active_id'))

    cours_id = fields.Many2one('ecole.cours',
                                string="Cours", required=True, default=_default_cours)
    prof_ids = fields.Many2many('ecole.prof', string="Profs")

    @api.multi
    def subscribe(self):
        self.cours_id.prof_id |= self.prof_id
        return {}
