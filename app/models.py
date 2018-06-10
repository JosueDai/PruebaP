from __future__ import unicode_literals

from django.db import models

# Create your models here.
class profesor(models.Model):
    idProfesor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)
    edad = models.IntegerField()
    asignatura = models.CharField(max_length=15)
    correo = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=15)


class clase(models.Model):
    clave = models.CharField(max_length=10,primary_key=True)
    idProfesor= models.ForeignKey(profesor, on_delete=models.CASCADE)
    nomClase=models.CharField(max_length=30)
    nHoras = models.IntegerField()  
class alumno(models.Model):
    idAlumno = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    carrera = models.CharField(max_length=40)
    correo= models.CharField(max_length=40)
    numero= models.CharField(max_length=20)
    contraseña=models.CharField(max_length=40)

class datos(models.Model):
    idMateria=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=80)
    descripcion=models.CharField(max_length=130)


