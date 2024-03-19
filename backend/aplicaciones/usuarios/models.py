from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class TipoUsuario(models.Model):

    TIPO_USUARIO = [
        ('admin', 'admin'),
        ('usuario', 'usuario'),
    ]

    descripcion_usuario = models.CharField(choices=TIPO_USUARIO, default=2, unique=True, blank=False, null=False)

    def __str__(self):
        return self.get_descripcion_usuario_display()


class Usuario(AbstractUser):
    
    nombre = models.CharField(max_length=250)
    apellido_paterno = models.CharField(max_length=250)
    apellido_materno = models.CharField(max_length=250)
    password = models.CharField(blank=False, null=False)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, blank=False, null=False,  default=2)

    def __str__(self):
        return self.nombre + ' ' + self.apellido_paterno + ' ' + self.apellido_materno