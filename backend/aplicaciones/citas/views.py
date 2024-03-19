from django.shortcuts import render
from rest_framework import viewsets
from .models import Cita
from .serializer import CitaSerializer

# Create your views here.
class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    