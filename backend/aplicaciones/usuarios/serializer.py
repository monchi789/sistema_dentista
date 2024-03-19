from .models import TipoUsuario, Usuario
from rest_framework import serializers

# Serializador para las clases de la aplicacion
class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'nombre', 'apellido_paterno', 'apellido_materno', 'email', 'password', 'id_tipo_usuario']