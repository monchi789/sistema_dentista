from django.contrib import admin
from .models import Tratamiento, Paciente, Pago

# Register your models here.
admin.site.register(Tratamiento)
admin.site.register(Paciente)
admin.site.register(Pago)
