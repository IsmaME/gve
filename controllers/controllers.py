# -*- coding: utf-8 -*-
# from odoo import http


# class Gve(http.Controller):
#     @http.route('/gve/gve', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gve/gve/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gve.listing', {
#             'root': '/gve/gve',
#             'objects': http.request.env['gve.gve'].search([]),
#         })

#     @http.route('/gve/gve/objects/<model("gve.gve"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gve.object', {
#             'object': obj
#         })
