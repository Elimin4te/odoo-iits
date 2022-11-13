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