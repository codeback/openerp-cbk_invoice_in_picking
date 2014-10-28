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

{
    'name' : 'Invoice reference in pickings',
    'version' : '0.1',
    'author': 'Codeback Software',
    'summary': 'Invoice reference for pickings',
    'description' : 'Invoice reference for invoiced pickings ',
    'depends' : ['stock'],
    'category': 'Warehouse',    
    'data': [],
    'update_xml': [
        'stock_picking_view.xml',
    ],
    'init_xml': [],
    'installable' : True,
    'active' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

