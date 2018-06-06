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


class cliente(models.Model):
    clave = models.CharField(max_length=10,primary_key=True)
    idPersona= models.ForeignKey(profesor, on_delete=models.CASCADE)
    ncompras = models.IntegerField()    