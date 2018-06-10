
from django.urls import path
from . import views

urlpatterns = [
    path('eliminar', views.eliminar),     
    path('consulta/modificacion/', views.modificacion),
    path('consulta/', views.consulta),
    path('menuP', views.menuP),
    path('RegClase', views.guardaClase),
    path('RegProfesor', views.guardarPersona),
    path('sumar',views.sumar),
    path('',views.index),
    path('nombre',views.nombre),
    path('esclava',views.esclava),
   path('modificar/', views.modificar), 

      
    path('consultaAl/modificaAlumno/',views.modificaAlumno),   
    path('consultaAl/', views.consultaAl),       
    path('elimina', views.elimina),        
    path('consul', views.consultaAl),    
    path('guardarAlumno', views.guardarAlumno), 

]