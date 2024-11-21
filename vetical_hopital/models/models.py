# -*- coding: utf-8 -*-
from odoo import models, fields, api, _ 
from odoo.exceptions import ValidationError
import re

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Habilitar Chatter y actividades

    # Identificación única del paciente
    name = fields.Char(
        string="Secuencia", 
        required=True, 
        readonly=True, 
        copy=False, 
        default=lambda self: _('New'), 
        tracking=True
    )

    # Nombre completo del paciente
    full_name = fields.Char(
        string="Name",
        required=True,
        tracking=True,
        default=lambda self: _('')  
    )

    # Apellido del paciente
    last_name = fields.Char(
        string="Last Name",
        required=True,
        tracking=True,
        default=lambda self: _('')  
    )
    
    # Registro Nacional de Contribuyentes (RNC)
    rnc = fields.Char(
        string="RNC", 
        tracking=True,
        required=True
    )

    # Relación con tratamientos
    treatment_ids = fields.Many2many(
        'hospital.treatment', 
        string="Treatments", 
        tracking=True,
        required=True
    )

    # Fecha de admisión
    date_time_admission = fields.Datetime(
        string="Admission Date", 
        default=fields.Datetime.now, 
        required=True, 
        tracking=True
    )

    # Fecha de última actualización
    date_time_update = fields.Datetime(
        string="Update Date", 
        readonly=True,
        tracking=True
    )

    # Estado del paciente
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('admitted', 'Admitted'),
            ('discharged', 'Discharged'),
        ],
        string="Estado", 
        default="draft", 
        tracking=True
    )
    
    # Modelo tratamientos
    class HospitalTreatment(models.Model):
        _name = 'hospital.treatment'
        _description = 'Hospital Treatment'

        name = fields.Char(
            string="Treatment Name",
            required=True
        )
        description = fields.Text(
            string="Description"
        )

    # Métodos
    
#Nombre y apellidos solo pueden usar letras
    @api.constrains('full_name', 'last_name')
    def _check_only_letters(self):
        """Valida que solo se puedan ingresar letras y espacios en los campos 'full_name' y 'last_name'"""
        pattern = re.compile("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")  # Permite letras, tildes, ñ y espacios
        for record in self:
            full_name = record.full_name.strip()  # Eliminar espacios en blanco extra
            last_name = record.last_name.strip()  # Eliminar espacios en blanco extra
            if full_name and not pattern.match(full_name):
                raise ValidationError("El nombre solo debe contener letras, tildes, ñ y espacios.")
            if last_name and not pattern.match(last_name):
                raise ValidationError("El apellido solo debe contener letras, tildes, ñ y espacios.")
#Nombre y apellidos solo pueden usar letras END

#RNC solo puede tener numeros
    @api.constrains('rnc')
    def _check_rnc_is_9_digits(self):
        """Valida que el campo 'rnc' contenga exactamente 9 números"""
        pattern = re.compile("^[0-9]{9}$")  # Solo permite exactamente 9 números
        for record in self:
            rnc = record.rnc.strip()  # Elimina espacios antes y después
            if rnc and not pattern.match(rnc):
                raise ValidationError("El RNC debe contener exactamente 9 números.")
#RNC solo puede tener numeros END


# Crear el ID automáticamente
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            # Usar la secuencia definida
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        return super(HospitalPatient, self).create(vals)
# Crear el ID automáticamente END

# Actualizar la fecha de modificación al editar cualquier campo
    def write(self, vals):
        """Actualiza la fecha de modificación al editar cualquier campo."""
        vals['date_time_update'] = fields.Datetime.now()  # Actualiza siempre que se haga un cambio
        return super(HospitalPatient, self).write(vals)
    
#Cambiar estados
    def action_admit(self):
        """Cambia el estado a 'admitted'."""
        self.write({'state': 'admitted'})
#Cambiar estados ENDS


    def action_discharge(self):
        """Cambia el estado a 'discharged'."""
        self.write({'state': 'discharged'})
#Cambiar estados END
