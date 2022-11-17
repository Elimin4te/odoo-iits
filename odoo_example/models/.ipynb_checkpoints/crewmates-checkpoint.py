# -*- coding: utf-8 -*-

from odoo import models, api, fields
from odoo.exceptions import ValidationError
from datetime import datetime as d

min_age = 21

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
        required=True,
        string='Birth Date', 
        help="Crewmate's Birth Date.",
        default="2000-10-10"
    )
    
    age = fields.Integer(
        string='Age', 
        help="Crewmate's age.",
        compute='set_age',
        store=True
    )
    
    join_date = fields.Date(
        required=True,
        string='Join Date', 
        help="The date Crewmate joined the org.",
        default="2020-10-10"
    )
    
    service_years = fields.Integer(
        string='Service Years', 
        help="Years since the crewmate joined.",
        compute='set_service_years',
        store=True
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
    
    current_mission = fields.Many2one(
        comodel_name = 'example.missions',
        string = "Current Mission",
        help = "The current mission the Crewmate is assigned to.",
        ondelete="set null",
        required = False,
        store=True,
        default=None
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
    
    @api.depends('birth_date')
    def set_age(self):
        
        for record in self:
            _cyear = int(d.now().date().year)
            _byear = int(record.birth_date.year)
            record.age = _cyear - _byear
            
    @api.constrains('age')
    def _check_age(self):
        
        for record in self:
            if record.age < min_age:
                raise ValidationError(
                        f"Sorry! the minimum age to join Crewmates is 21."
                )
            
    @api.depends('join_date')       
    def set_service_years(self):
        
        for record in self:
            _cyear = int(d.now().date().year)
            _jyear = int(record.join_date.year)
            record.service_years = _cyear - _jyear
    
    @api.constrains('join_date')
    def _check_dates(self):
        
        for record in self:
            if (record.birth_date) >= (record.join_date):
                raise ValidationError(
                        f"Whoops! might've been a typo, but you specified a lower Join Date than Birth Date, try again."
                    )
                    
   
            