# -*- coding: utf-8 -*-

from odoo import models, api, fields
from odoo.exceptions import ValidationError
from datetime import datetime as d

class Missions(models.Model):
    
    _name = 'example.missions'
    _description = 'This Model represents the Mission dataclass.'
    
    name = fields.Char(
        required=True,
        string='Name',
        help='Mission Name'
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
        string='Starting Date',
        help='Appr. Date this mission will start.',
        default="2020-10-10",
        required=True
    )
    
    end_date = fields.Date(
        string='Ending Date',
        help='Appr. Date this mission will end.',
        default="2025-10-10",
        required=True
    )
    
    duration_years = fields.Integer(
        required=False,
        string='Approx. Duration',
        help='Appr. duration in years for the mission.',
        store=True,
        compute='set_duration'
    )
    
    required_personal = fields.Integer(
        required=True,
        string='Minimum Crewmates',
        help='Minimum Crewmates required for the Mission.',
        default=3
    )
    
    mission_crewmates = fields.One2many(
        required=False,
        string='Crewmates',
        help='Crewmates assigned to this mission.',
        default=None,
        comodel_name='example.crewmates',
        inverse_name='current_mission',
        store=True
    )
    
    mission_share = fields.One2many(
        required=False,
        string='Share',
        help='Mission Shares.',
        default=None,
        comodel_name='mission.shares',
        inverse_name='mission_id',
        store=True
    )
    
    assigned_spaceship = fields.Many2one(
        'res.partner',
        required=False,
        string='Spaceship',
        help='The assigned spaceship for this mission.',
        default=None,
        store=True
    )
    
    @api.constrains('goal', 'description')
    def _check_lenght(self):
        
        for record in self:
            if len(record.description.replace(' ','')) < 30:
                raise ValidationError(
                    f"Too short! Description Field lenght should be 30 letters at least (not inluding spaces), but you entered {len(record.description.replace(' ',''))}."
                )
             
            if len(record.goal.replace(' ','')) < 20:
                raise ValidationError(
                    f"Too short! Goal Field lenght should be 30 letters at least (not inluding spaces), but you entered {len(record.goal.replace(' ',''))}."
                )
                
    @api.constrains('end_date')
    def _check_end_date(self):
        
        for record in self:
            if (record.end_date) <= (record.start_date):
                raise ValidationError(
                    f"Watch out! End Date field can't be lower or equal to Start Date."
                )
                
    @api.depends('start_date', 'end_date')
    def set_duration(self):
        
        for record in self:
            _syear = int(record.start_date.year)
            _fyear = int(record.end_date.year)
            record.duration_years = _fyear - _syear
    