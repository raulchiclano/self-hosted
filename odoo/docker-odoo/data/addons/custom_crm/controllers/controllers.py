# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/customCrm(http.Controller):
#     @http.route('//mnt/extra-addons/custom_crm//mnt/extra-addons/custom_crm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/custom_crm//mnt/extra-addons/custom_crm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/custom_crm.listing', {
#             'root': '//mnt/extra-addons/custom_crm//mnt/extra-addons/custom_crm',
#             'objects': http.request.env['/mnt/extra-addons/custom_crm./mnt/extra-addons/custom_crm'].search([]),
#         })

#     @http.route('//mnt/extra-addons/custom_crm//mnt/extra-addons/custom_crm/objects/<model("/mnt/extra-addons/custom_crm./mnt/extra-addons/custom_crm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/custom_crm.object', {
#             'object': obj
#         })
