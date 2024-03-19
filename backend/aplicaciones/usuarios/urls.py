from django.urls import path, include
from .views import TipoUsuarioViewSet, UsuarioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tipo-usuario', TipoUsuarioViewSet)
router.register('usuario', UsuarioViewSet)

urlpatterns = [
    path('usuarios/', include(router.urls)),
]
