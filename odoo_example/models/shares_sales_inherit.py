# -*- coding: utf-8 -*-

from odoo import models, api, fields

class SaleOrder(models.Model):
    _inherit = ['sale.order']
    
    share_id = fields.Many2one(
        comodel_name = 'mission.shares',
        string = 'Related Mission',
        ondelete = 'cascade',
    )
    
    is_share = fields.Boolean(
        string='Is a Mission Share',
        default=False
    )
    
    
    