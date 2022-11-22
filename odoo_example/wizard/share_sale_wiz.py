# -*- coding: utf-8 -*-

from odoo import models, api, fields

class ShareSaleWiz(models.TransientModel):
    
    _name = 'mission.shares.wizard'
    _description = 'Transient model for Share Sale Wizard'
    
    def _default_share(self):
        return self.env['mission.shares'].browse(self._context.get('active_id'))
    
    share_id = fields.Many2one(
        comodel_name = 'mission.shares',
        string = 'Share ID',
        help = 'The share this model refers to.',
        required=True,
        default=_default_share
    )
    
    investors = fields.Many2many(
        related = 'share_id.investors',
        string = 'Investors/Sponsors',
        help = 'Mission sponsors and investors.',
        ondelete = 'cascade',
        required = True,
    )
    
    buyers = fields.Many2many(
        comodel_name = 'res.partner',
        string = 'Buyers',
        required = True
    )
    
    qty = fields.Integer(
        string="Buy QTY.",
        help="Amount of shares to buy.",
        required=True,
        default=10
    )
    
    def create_sale_order(self):
        
        share_product_id = self.env['product.product'].search([('is_share','=',True)], limit=1)
        if share_product_id:
            for x in self.buyers:
                order_id = self.env['sale.order'].create({
                    'partner_id': x.id,
                    'share_id': self.share_id.id,
                    'is_share': True,
                    'order_line': [(0, 0, {'product_id': share_product_id.id, 'product_uom_qty': self.qty, 'price_unit': self.share_id.fprice})]
                })