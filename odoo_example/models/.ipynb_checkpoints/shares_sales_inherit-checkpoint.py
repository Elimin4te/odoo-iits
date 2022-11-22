# -*- coding: utf-8 -*-

from odoo import models, api, fields

class SaleOrder(models.Model):
    _inherit = ['sale.order']
    
    share_id = fields.Many2one(
        comodel_name = 'mission.shares',
        string = 'Related Mission',
        ondelete = 'cascade',
    )
    
    qty = fields.Integer(
        string="Buy QTY.",
        help="Amount of shares to buy.",
        required=True,
        default=10
    )
    
    is_share = fields.Boolean(
        string='Is a Mission Share',
        default=False
    )
    
    
    