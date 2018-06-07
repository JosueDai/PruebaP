
from django.urls import path
from . import views

urlpatterns = [
    path('eliminar', views.eliminar),
    path('modificar/', views.modificar),
    path('consulta/modificacion/', views.modificacion),
    path('consulta/', views.consulta),
    path('menuP', views.menuP),
    path('RegClase', views.guardaClase),
    path('guardarAlumno', views.guardarAlumno),
    path('RegProfesor', views.guardarPersona),
    path('sumar',views.sumar),
    path('',views.index),
    path('nombre',views.nombre),
    path('esclava',views.esclava)



]