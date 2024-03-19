from django.urls import path, include
from rest_framework import routers
from .views import PacienteViewSet, TratamientoViewSet, PagoViewSet

router = routers.DefaultRouter()
router.register('paciente', PacienteViewSet)
router.register('tratamiento', TratamientoViewSet)
router.register('pago', PagoViewSet)

urlpatterns = [
    path('tratamientos/', include(router.urls))
]
