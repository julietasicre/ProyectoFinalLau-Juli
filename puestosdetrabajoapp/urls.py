from django.urls import path
from . import views

urlpatterns = [
    path('gerente/crear', views.crear_gerente, name='crear_gerente'),
    # path ('', name='buscar_gerente')
]
