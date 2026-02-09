# -*- coding: utf-8 -*-
# from odoo import http


# class VigoTech(http.Controller):
#     @http.route('/vigo_tech/vigo_tech', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vigo_tech/vigo_tech/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vigo_tech.listing', {
#             'root': '/vigo_tech/vigo_tech',
#             'objects': http.request.env['vigo_tech.vigo_tech'].search([]),
#         })

#     @http.route('/vigo_tech/vigo_tech/objects/<model("vigo_tech.vigo_tech"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vigo_tech.object', {
#             'object': obj
#         })

