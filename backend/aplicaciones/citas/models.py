from django.db import models
from ..tratamientos.models import Paciente

# Create your models here.
class Cita(models.Model):

    fecha = models.DateField(null=False, blank=False)
    hora = models.TimeField(null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)

    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return str(self.fecha) + ' ' + str(self.hora)