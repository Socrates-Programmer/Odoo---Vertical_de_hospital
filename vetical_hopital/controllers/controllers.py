# -*- coding: utf-8 -*-
# from odoo import http


# class VeticalHopital(http.Controller):
#     @http.route('/vetical_hopital/vetical_hopital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vetical_hopital/vetical_hopital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vetical_hopital.listing', {
#             'root': '/vetical_hopital/vetical_hopital',
#             'objects': http.request.env['vetical_hopital.vetical_hopital'].search([]),
#         })

#     @http.route('/vetical_hopital/vetical_hopital/objects/<model("vetical_hopital.vetical_hopital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vetical_hopital.object', {
#             'object': obj
#         })

