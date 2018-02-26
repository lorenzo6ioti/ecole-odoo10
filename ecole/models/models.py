# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api, exceptions


class Prof(models.Model):
    _name = "ecole.prof"
    name = fields.Char(string="Nom", required=True)
    age = fields.Integer(string="Age")
    date_naissance = fields.Date(default=fields.Date.today)
    retraite = fields.Boolean(string="Retraité", default=False)
    section_id = fields.Many2one('ecole.section', string="Section")
    cours_ids = fields.One2many('ecole.cours', 'titulaire_id', string="Liste des cours")


class Cours(models.Model):
    _name = "ecole.cours"
    name = fields.Char(string="Nom", required=True)
    nbHeures = fields.Integer(string="Nombre d'heures", required=True)
    nbEleves = fields.Integer(string="Nombre d'élèves", compute="_nbplaces", store=True)
    nbPlaces = fields.Integer(string="Nombre de places disponibles")
    date_debut = fields.Date(default=fields.Date.today)
    date_fin = fields.Date(string="Date de fin", store=True, compute="_end_date", inverse="_set_end_date")
    taken_seats = fields.Float(string="Pourcentage de places occupées", compute="_pourcentplaces", default=10)
    titulaire_id = fields.Many2one('ecole.prof', string="Titulaire")
    eleve_ids = fields.Many2many('ecole.eleve',
        string="Eleves participants")

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Cours, self).copy(default)

    @api.depends('date_debut', 'nbHeures')
    def _set_end_date(self):
        for r in self:
            start = fields.Datetime.from_string(r.date_debut)
            end = fields.Datetime.from_string(r.date_fin)
            r.nbHeures = ((end - start).days + 1) * 24

    @api.depends('date_debut')
    def _end_date(self):
        for r in self:
            start = fields.Datetime.from_string(r.date_debut)
            duree = timedelta(days=(r.nbHeures / 24), seconds=-1)
            r.date_fin = start + duree

    @api.depends('eleve_ids')
    def _nbplaces(self):
        for r in self:
            r.nbEleves = len(r.eleve_ids)

    @api.depends('nbPlaces', 'nbEleves')
    def _pourcentplaces(self):
        for r in self:
            if r.nbEleves == 0:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * r.nbEleves / r.nbPlaces

    @api.onchange('nbEleves', 'nbPlaces')
    def _verif_valid_nbPlace(self):
        if self.nbPlaces < 0:
            return {
                'warning': {
                    'title': "Incorrect number of student value",
                    'message': "The number of student",
                },
            }
        elif self.nbEleves > self.nbPlaces:
            return {
                'warning': {
                    'title': "Surplus d'élèves",
                    'message': "Le nombre d'élèves inscrits est supérieur au nombre de places",
                },
            }

    @api.constrains('nbPlaces', 'nbEleves')
    def _check_nbEleves(self):
        for r in self:
            if r.nbEleves > r.nbPlaces:
                raise exceptions.ValidationError("Le nombre d'élèves ne peut être supérieur au nombre de places")


class Eleve(models.Model):
    _name = "ecole.eleve"
    name = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prenom", required=True)
    age = fields.Integer(string="Age")
    section_id = fields.Many2one('ecole.section', string="Section")
    cours_ids = fields.Many2many('ecole.cours', string="Liste des cours")


class Section(models.Model):
    _name = "ecole.section"
    name = fields.Char(string="Nom")
    eleve_ids = fields.One2many('ecole.eleve', 'section_id', string="Eleves")
    prof_ids = fields.One2many('ecole.prof', 'section_id', string="Profs")
