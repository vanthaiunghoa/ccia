# -*- coding: utf-8 -*-
from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT
from openerp.exceptions import Warning
import time
from odoo.exceptions import UserError
import odoo.addons.decimal_precision as dp
from openerp.osv import osv
import base64
from odoo import models, fields, api
from datetime import datetime, timedelta
import codecs
values = {}

import datetime

class sale_order_inherit(models.Model):
	_inherit = 'sale.order'
	event_id = fields.Many2one('event.event','Evento')
	event_id_count = fields.Integer(string='Eventos', compute='_compute_eventos_ids')
	event_name = fields.Char(string='Nombre del Evento')
	evento_start_date = fields.Datetime(string='Fecha Inicio del Evento')
	evento_end_date = fields.Datetime(string='Fecha Final del Evento')

	@api.multi
	@api.depends('event_id')
	def _compute_eventos_ids(self):
		for order in self:
			order.event_id_count = len(order.event_id)

	@api.multi
	def action_view_event(self):
		'''
		esta funcion abre un tree si es que hay mas de un elemento
		y si solo hay uno abre el form con el elemento vinculado
		'''
		action = self.env.ref('event.action_event_view').read()[0]

		pickings = self.mapped('event_id')
		if len(pickings) > 1:
			action['domain'] = [('id', 'in', pickings.ids)]
		elif pickings:
			action['views'] = [(self.env.ref('event.view_event_form').id, 'form')]
			action['res_id'] = pickings.id
		return action

	@api.multi
	def action_confirm(self):
		t = super(sale_order_inherit,self).action_confirm()
		if self.event_name and self.evento_start_date and self.evento_end_date:
			print('entro a order')
			fecha_inicial = self.evento_start_date
			fecha_end = self.evento_end_date
			name_event= self.event_name
			cotizacion = self.id
			vals = {
				'name':name_event,
				'date_begin':fecha_inicial,
				'date_end':fecha_end,
				'sale_order_id':self.id,
			}
			wizard = self.env['event.event'].create(vals)
			self.event_id=wizard.id

		return t


class event_event_inherit(models.Model):
	_inherit = 'event.event'

	sale_order_id = fields.Many2one('sale.order','Cotizacion')
	sale_order_count = fields.Integer(string='Cotizaciones', compute='_compute_sale_order_ids')

	partner_id = fields.Many2one('res.partner', 'Cliente',related='sale_order_id.partner_id')
	
	contact = fields.Many2one('res.partner', related='sale_order_id.partner_order_id')
	contact_mail = fields.Char('Email de Contacto', related='contact.email')
	contact_phone = fields.Char('Telefono de Contacto', related='contact.phone')
	contact_mobile = fields.Char('Celular de Contacto', related='contact.mobile')
	equipos_evento = fields.Text('Equipos')
	arreglo_evento = fields.Text('Arreglo')
	observaciones_event = fields.Text('Observaciones')

	@api.multi
	@api.depends('sale_order_id')
	def _compute_sale_order_ids(self):
		for order in self:
			order.sale_order_count = len(order.sale_order_id)
	
	@api.multi
	def action_view_sale_order(self):
		action = self.env.ref('sale.action_orders').read()[0]
		pickings = self.mapped('sale_order_id')
		if len(pickings) > 1:
			action['domain'] = [('id', 'in', pickings.ids)]
		elif pickings:
			action['views'] = [(self.env.ref('sale.view_order_form').id, 'form')]
			action['res_id'] = pickings.id
		return action
