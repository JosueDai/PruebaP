
from django.urls import path
from . import views

urlpatterns = [
    path('modificar',views.modificar),
    path('editar', views.editar),
    path('consulta', views.consulta),
    path('menuP', views.menuP),
    path('guardarPersona', views.guardarPersona),
    path('sumar',views.sumar),
    path('',views.index),
    path('nombre',views.nombre),
    path('esclava',views.esclava)



]