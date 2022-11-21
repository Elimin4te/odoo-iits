# -*- coding: utf-8 -*-

from odoo import models, api, fields

class SaleOrder(models.Model):
    _inherit = ['sale.order']
    
    mission_id = fields.Many2one(
        comodel_name = 'example.missions',
        string = 'Related Mission',
        ondelete = 'cascade',
    )
    
    crewmates_id = fields.One2many(
        string='Crewmates',
        related = 'mission_id.mission_crewmates',
    )
    
    is_share = fields.Boolean(
        string='Is a Mission Share',
        default=False
    )
    
    
    