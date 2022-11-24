# -*- coding: utf-8 -*-

from odoo import http

class ShareSales(http.Controller):
    
    @http.route(
        '/SpaceMission/', 
        auth='public', 
        website=True
    )
    def index(self, **kwargs): 
        return 'Hello World!'
    
    @http.route(
        '/SpaceMission/missions/', 
        auth='public', 
        website=True
    )
    def missions(self, **kwargs): 
        missions = http.request.env['example.missions'].search([])
        return http.render(
            'odoo_example.missions_website', 
            {'missions': missions}
        )
    