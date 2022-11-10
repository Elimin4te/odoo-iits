# -*- coding: utf-8 -*-

from odoo import models, api, fields

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
    
    is_new = fields.Boolean(
        string='New', 
        help="Whether the Crewmate recently joined or not. Default is False.",
        default=False,
        copy=False
    )
    
    completed_missions = fields.Integer(
        string='Completed Missions', 
        help="Crewmate's amount of completed missions. Default is 0.",
        default=0
    )
    
    # current_mission = fields.many2one('example.missions', 'Missions')
    
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