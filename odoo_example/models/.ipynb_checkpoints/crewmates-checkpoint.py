# -*- coding: utf-8 -*-

from odoo import models, api, fields
from odoo.exceptions import ValidationError
from datetime import datetime as d

vald_date = d(2001, 11, 13).date()

nationality_selection = [
    ('ve', 'Venezuela'),
    ('usa', 'United States of America'),
    ('arg', 'Argentine'),
    ('esp', 'Spain'),
]

agency_selection = [
    ('cia', 'CIA'),
    ('fanb', 'FANB'),
    ('fbi', 'FBI'),
    ('nasa', 'NASA'),
]



class Crewmates(models.Model):
    
    _name = 'example.crewmates'
    _description = 'This model defines the Crewmate dataclass.'
    # _auto = True
    
    full_name = fields.Char(
        required=True, 
        string='Name', 
        help="Crewmate's name."
    )
    
    birth_date = fields.Date(
        string='Birth Date', 
        help="Crewmate's Birth Date."
    )
    
    join_date = fields.Date(
        string='Join Date', 
        help="The date Crewmate joined the org."
    )
    
    nationality = fields.Selection(
        string='Nationality', 
        help="Crewmate's Nationality.",
        selection=nationality_selection
    )
    
    agency = fields.Selection(
        string='Agency', 
        help="Crewmate's Agency.",
        selection=agency_selection,
        copy=False
    )
    
    completed_missions = fields.Integer(
        string='Completed Missions', 
        help="Crewmate's amount of completed missions. Default is 0.",
        default=0
    )
    
    role = fields.Char(
        required=True, 
        string='Role', 
        help="Crewmate's role in the mission (engineer, medical staff...).",
    )
    
    height_meters = fields.Float(
        required=True,
        string='Height', 
        help="Crewmate's height in meters."
    )
    
    weight_kg = fields.Float(
        required=True,
        string='Weight', 
        help="Crewmate's weight in KGs."
    )
    
    IQ = fields.Integer(
        required=True,
        string='IQ', 
        help="Crewmate's Intellectual Coeficient."
    )
    
    @api.constrains('IQ', 'weight_kg', 'height_meters')
    def _check_physical(self):
        
        for record in self:
            if record.IQ < 160:
                raise ValidationError(
                    f"Sorry, only prospects with 160+ IQ can join the Crewmates! your's is {record.IQ}."
                )
            if record.weight_kg > 90:
                raise ValidationError(
                    f"Sorry, you seem a little too thick to join the Crewmates."
                )
            if record.height_meters < 1.60:
                raise ValidationError(
                    f"Sorry, only prospects higher than 1.60m can join the Crewmates! your's is {record.height_meters}m."
                )
    
    @api.constrains('birth_date', 'join_date')
    def _check_dates(self):
        
        for record in self:
            if (record.birth_date) > vald_date:
                raise ValidationError(
                    f"Sorry, minimal age to join the Crewmates is 21."
                )
            else:
                if (record.birth_date) >= (record.join_date):
                    raise ValidationError(
                        f"Whoops! might've been a typo, but you specified a lower Join Date than Birth Date, try again."
                    )