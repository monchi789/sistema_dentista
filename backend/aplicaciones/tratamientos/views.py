from django.shortcuts import render
from rest_framework import viewsets
from .models import Pago, Paciente, Tratamiento
from .serializer import PacienteSerializer, PagoSerializer, TratamientoSerializer

# Create your views here.
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
