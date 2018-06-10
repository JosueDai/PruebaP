
from django.urls import path
from . import views

urlpatterns = [
    path('eliminar', views.eliminar),     
    path('consulta/modificacion/', views.modificacion),
    path('consulta/', views.consulta),
    path('menuP', views.menuP),
    path('RegClase', views.guardaClase),
    path('RegProfesor', views.guardarPersona),
#========HEAD
    path('sumar',views.sumar),
    path('',views.index),
    path('nombre',views.nombre),
    path('esclava',views.esclava),
   path('modificar/', views.modificar), 
#=======

    path('guardarMat/', views.guardarMat),
    path('consultaMat', views.consultaMat),
    path('modificarMa', views.modificarMa),
    path('editarMa', views.editarMa),
    #=========== a6cc623a3c4fcf9a9127ced7bc303047b7cbc573

      
    path('consultaAl/modificaAlumno/',views.modificaAlumno),   
    path('consultaAl/', views.consultaAl),       
    path('elimina', views.elimina),        
    path('consul', views.consultaAl),    
    path('guardarAlumno', views.guardarAlumno), 

]