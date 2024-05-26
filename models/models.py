# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Vehiculo(models.Model):
    _name = 'gve.vehiculo'
    _description = 'gve.vehiculo'
    _rec_name = 'matricula'    
    
    #info general
    imagenVehiculo = fields.Binary(attachment=True)
    matricula = fields.Char()
    tipoVehiculo = fields.Selection([('furgon', 'Furgón'), ('camion', 'Camión'), ('turismo', 'Turismo'), ('motocicleta', 'Motocicleta'), ('ciclomotor', 'Ciclomotor')])
    marca = fields.Char()
    modelo = fields.Char()
    fechaProduccion = fields.Date()
    fechaEntrada = fields.Date()
    combustible = fields.Selection([('diesel', 'Diesel'), ('gasolina', 'Gasolina'), ('electrico', 'Eléctrico')])  

    #Estado del vehiculo
    renting = fields.Boolean(default = False)
    segundamano = fields.Boolean(default = False)
    kilometraje = fields.Float()
    averia = fields.Boolean(default=False)
    tipoAveria = fields.Selection([('mecanica', 'Mecánica'), ('electrica', 'Eléctrica'), ('neumatica', 'Neumática')])
    descripcionAveria = fields.Text()
    puedeCircular = fields.Boolean(default = False)

    anotaciones = fields.Text()
    
    #relacion
    persona = fields.One2many("gve.persona","Vehiculo")
    
class Persona(models.Model):
    _name = 'gve.persona'
    _description = 'gve.persona'
    _rec_name = 'dni'  

    dni = fields.Char()
    nombre = fields.Char()
    apellido = fields.Char()

    permisob = fields.Boolean()
    permisoc = fields.Boolean()
    permisoa = fields.Boolean()

    #relacion
    Vehiculo = fields.Many2one("gve.vehiculo")