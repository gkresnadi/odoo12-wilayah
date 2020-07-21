# -*- coding: utf-8 -*-
from odoo import http

# class SrtWilayah(http.Controller):
#     @http.route('/srt_wilayah/srt_wilayah/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/srt_wilayah/srt_wilayah/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('srt_wilayah.listing', {
#             'root': '/srt_wilayah/srt_wilayah',
#             'objects': http.request.env['srt_wilayah.srt_wilayah'].search([]),
#         })

#     @http.route('/srt_wilayah/srt_wilayah/objects/<model("srt_wilayah.srt_wilayah"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('srt_wilayah.object', {
#             'object': obj
#         })