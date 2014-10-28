# -*- encoding: utf-8 -*-
##############################################################################
#
#    incoming_provider_reference: Adds the provider reference for
#                                 incoming shipments.
#    Copyright (c) 2013 Codeback Software S.L. (http://codeback.es)    
#    @author: Miguel García <miguel@codeback.es>
#    @author: Javier Fuentes <javier@codeback.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields,osv

class stock_picking(osv.osv):
	
    _inherit = "stock.picking"
    _order = 'id desc'
    _columns = {
        'invoice_id': fields.many2one('account.invoice', 'Invoice', readonly=True),
        'internal_number': fields.related('invoice_id', 'number', type='char', string='Invoice Number', readonly=True)
    }

class stock_picking_out(osv.osv):
    
    _inherit = "stock.picking.out"
    _order = 'id desc'
    _columns = {
        'invoice_id': fields.many2one('account.invoice', 'Invoice', readonly=True),
        'internal_number': fields.related('invoice_id', 'number', type='char', string='Invoice Number', readonly=True)
    }