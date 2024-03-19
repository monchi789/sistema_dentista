from django.db import models
from ..usuarios.models import Usuario


# Create your models here.
class Paciente(models.Model):
    
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido_paterno = models.CharField(max_length=50, null=False, blank=False)
    apellido_materno = models.CharField(max_length=50, null=False, blank=False)
    telefono = models.CharField(max_length=9, null=False, blank=False)
    dni = models.CharField(max_length=8, null=False, blank=False)

    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno
    

class Tratamiento(models.Model):

    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    costo = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    monto_pagado = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    estado = models.BooleanField(null=False, blank=False)

    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.nombre
    

class Pago(models.Model):
    
        fecha = models.DateField(null=False, blank=False)
        monto = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    
        id_tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE, null=False, blank=False)
    
        def __str__(self):
            return self.monto