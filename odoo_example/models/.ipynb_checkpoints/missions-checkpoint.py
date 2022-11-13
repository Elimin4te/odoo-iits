# -*- coding: utf-8 -*-

from odoo import models, api, fields

class Missions(models.Model):
    
    _name = 'example.missions'
    _description = 'This Model represents the Mission dataclass.'
    
    name = fields.Char(
        required=True,
        string='Name',
        help='Mission Name.'
    )
    
    description = fields.Text(
        required=True,
        string='Description',
        help="Mission Description."
    )
   
    goal = fields.Text(
        required=True,
        string='Goal',
        help="Mission Goal."
    )
    
    start_date = fields.Date(
        required=True,
        string='Starting Date',
        help='Appr. Date this mission will start.'
    )
    
    end_date = fields.Date(
        required=True,
        string='Ending Date',
        help='Appr. Date this mission will end.'
    )
    
    required_personal = fields.Integer(
        required=True,
        string='Minimum Crewmates',
        help='Minimum Crewmates required for the Mission.',
        default=3
    )