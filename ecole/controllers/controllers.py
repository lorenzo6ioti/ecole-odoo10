# -*- coding: utf-8 -*-
from odoo import http
# class Ecole(http.Controller):
#     @http.route('/ecole/ecole/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ecole/ecole/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ecole.listing', {
#             'root': '/ecole/ecole',
#             'objects': http.request.env['ecole.ecole'].search([]),
#         })

#     @http.route('/ecole/ecole/objects/<model("ecole.ecole"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ecole.object', {
#             'object': obj
#         })
