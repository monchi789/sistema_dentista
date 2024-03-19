from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TipoUsuario, Usuario

# Register your models here.
admin.site.register(TipoUsuario)
admin.site.register(Usuario, UserAdmin)