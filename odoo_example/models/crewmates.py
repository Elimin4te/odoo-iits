# -*- coding: utf-8 -*-

from odoo import models, api, fields

class Crewmates(models.Model):
    
    _name = 'example.Crewmates'
    _description = 'This model defines the Crewmate dataclass.'
    _auto = True
    
    full_name = fields.Char()
    birth_date = fields.Date()
    join_date = fields.Date()
    is_new = fields.Boolean()
    completed_missions = fields.Integer()
    # current_mission = fields.many2one('example.Missions', 'Missions')
    role = fields.Char()
    