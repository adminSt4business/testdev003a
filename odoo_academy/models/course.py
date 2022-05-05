# _*_ coding: utf-8 _*_
from odoo import models, fields, api

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description', required=True)
    level = fields.Selection(string='Level',
                             selection=[('beginer','Beginer'),
                                        ('intermediate','Intermediate'),
                                        ('advanced','Advanced')
                                       ],
                             copy=False, 
                             required=True
                            )
    active = fields.Boolean(string='Active', default=True)