from django.urls import path, include
from rest_framework import routers
from .views import CitaViewSet

router = routers.DefaultRouter()

router.register('cita', CitaViewSet)

urlpatterns = [
    path('citas/', include(router.urls))
]