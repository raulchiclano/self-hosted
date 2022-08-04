# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Visit(models.Model):
     _name = 'custom_crm.visit'
     _description = 'Visit'

     name = fields.Char(string='Descripción')
     customer = fields.Many2one(string='Cliente', comodel_name="res.partner")
     date = fields.Datetime(string="Fecha")
     type = fields.Selection([('P','Presencial'), ('W', 'Whatsapp'), ('T', 'Telefónica'),('Z', 'Zoom')], string='Tipo', required=True)
     done = fields.Boolean(string='Realizada')
     regular = fields.Boolean(string='Prec. Regular', readonly=True)
     auxiliar = fields.Boolean(string='Prec. Auxiliar', readonly=True)
     
     
     def toggle_state(self):
          self.done = not self.done

     def toggle_regular(self):
          self.regular = not self.regular

     def toggle_auxiliar(self):
          self.auxiliar = not self.auxiliar