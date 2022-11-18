# -*- coding: utf-8 -*-

from odoo import models, api, fields
from odoo.exceptions import ValidationError

tax_pc = 0.16

class MissionShares(models.Model):
    
    _name = 'mission.shares'
    _description = "This model defines the mission's share dataclass."
    
    mission_id = fields.Many2one(
        comodel_name = 'example.missions',
        string = "Mission Name",
        help = "The mission this record refers to",
        ondelete="cascade",
        required = True,
        store=True
    )
    
    investors = fields.Many2many(
        comodel_name = 'example.missions',
        string = 'Investors/Sponsors',
        help = 'Mission sponsors and investors.',
        ondelete = 'cascade',
        required = True,
        store = True
    )
    
    qty = fields.Integer(
        string = 'Total Shares',
        help = 'Total shares this mission has.',
        required = True,
        default = 100_000_000
    )
    
    bprice = fields.Integer(
        string = 'Base Price',
        help = 'Base price for each share.',
        required = True,
        default = 100
    )
    
    tax = fields.Integer(
        string = 'Tax',
        help = 'Tax for each share.',
        compute = 'calc_pr',
        store = True
    )
    
    fprice = fields.Integer(
        string = 'Final Price',
        help = 'Final price for each share.',
        compute = 'calc_pr',
        store = True
    )
    
    reserved_shares = fields.Integer(
        string = 'Reserved Shares (%)',
        help = 'Reserved quantity of shares in %.',
        required = True,
        default = 20
    )
    
    total_reservation = fields.Integer(
        string = 'Reserved Shares QTY',
        compute = 'calc_total_shares',
        store = True
    )
    
    @api.constrains('reserved_shares')
    def _check_rs(self):
        
        for record in self:
            if record.reserved_shares >= 40:
                raise ValidationError("Reserved shares can't be higher than 40%!")
                
    @api.depends('bprice')
    def calc_pr(self):
        
        for record in self:
            record.tax = record.bprice*tax_pc
            record.fprice = record.tax + record.bprice
                
    @api.depends('reserved_shares', 'qty')
    def calc_total_shares(self):
        
        for record in self:
            record.total_reservation = record.qty*(record.reserved_shares/100)
            
            