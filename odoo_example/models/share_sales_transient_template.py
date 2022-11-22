# -*- coding: utf-8 -*-

from odoo import models, api, fields
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    
    _inherit = ['product.template']
    _description = 'Shares Product Template'
    
    """share_id = fields.Many2one(
        comodel_name = 'mission.shares',
        string = 'Share ID',
        help = 'The share this model refers to.',
        required=True
    )"""
    
    is_share = fields.Boolean(
        string='Is a Mission Share',
        default=False
    )