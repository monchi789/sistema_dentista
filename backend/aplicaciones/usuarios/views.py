from django.shortcuts import render
from .models import TipoUsuario, Usuario
from rest_framework import viewsets
from .serializer import TipoUsuarioSerializer, UsuarioSerializer

# Create your views here.
class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    