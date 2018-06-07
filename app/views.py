from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import get_template
# from django.template import Context
from . import persona
from . import models


# Create your views here.


def index(request):
    return render(request,'index.html')  

def guardarPersona(request):
    if 'idProfesor' in request.POST and 'nombre' in request.POST and 'edad' in request.POST and 'asignatura' in request.POST and 'correo' in request.POST and 'contraseña' in request.POST:
     idProfesor=request.POST['idProfesor']
     nombre=request.POST['nombre']
     edad=request.POST['edad']
     asignatura=request.POST['asignatura']
     correo=request.POST['correo']
     contraseña=request.POST['contraseña']
     p= models.profesor(idProfesor= idProfesor,nombre = nombre, edad = edad, asignatura=asignatura, correo=correo, contraseña=contraseña)
     p.save()     
     return render(request, 'menuProfesor.html',{'msg':'Registro realizado correctamente'})
    else:
        return render(request, 'regProfesor.html',{'msg': 'No se puede realizar registro'})    

def menuP (request):
     return render(request,'menuProfesor.html')

def consulta(request):
    registro = models.profesor.objects.all()
    return render(request,'consultapro.html',{"registro": registro })

def modificacion(request):
    if 'idProfesor' in request.POST:
        registro = models.profesor.objects.get(idProfesor=request.POST['idProfesor'])
        return render(request,'modificarpro.html',{"reg":registro})
    else:
        return redirect('consulta/')

def modificar(request):
    if 'idProfesor' in request.POST and 'nombre' in request.POST and 'edad' in request.POST and 'asignatura' in request.POST and 'correo' in request.POST and 'contraseña' in request.POST:
        p = models.profesor(idProfesor = request.POST['idProfesor'])
        p.nombre=request.POST['nombre']
        p.edad=request.POST['edad']
        p.asignatura=request.POST['asignatura']
        p.correo=request.POST['correo']
        p.contraseña=request.POST['contraseña']
        p.save()
    return redirect('/inicio/consulta', {'op':'Actualizacion Realizada'})

def eliminar(request):
    if 'idProfesor' in request.POST:
        per = models.profesor.objects.get(idProfesor=request.POST['idProfesor'])
        per.delete()
    return redirect('/inicio/consulta')

def guardarAlumno(request):
    if 'idAlumno' in request.POST and 'nombre' in request.POST and 'carrera' in request.POST and 'correo' in request.POST and 'numero' in request.POST and 'contraseña' in request.POST:
        idAlumno=request.POST['idAlumno']
        nombre=request.POST['nombre']
        carrera=request.POST['carrera']
        correo=request.POST['correo']
        numero=request.POST['numero']
        contraseña=request.POST['contraseña']
        p= models.alumno(idAlumno= idAlumno,nombre = nombre, carrera = carrera, correo=correo, numero=numero, contraseña=contraseña)
        p.save()     
        return render(request, 'menuAlumno.html',{'msg':'Registro realizado correctamente'})
    else:
        return render(request, 'regAlumno.html',{'msg': 'No se puede realizar registro'})  

def guardaClase(request):
    if 'clave' in request.POST and 'nomClase' in request.POST and 'nHoras' in request.POST and 'idProfesor' in request.POST:
        clave=request.POST['clave']
        nomClase=request.POST['nomClase']
        nHoras=request.POST['nHoras']
        idProfesor=request.POST['idProfesor']
        p= models.clase(clave= clave, nomClase = nomClase, nHoras=nHoras, idProfesor = idProfesor)
        p.save()     
        return render(request, 'menuProfesor.html',{'msg':'Registro realizado correctamente'})
    else:
        return render(request, 'regClase.html',{'msg': 'No se puede realizar registro'})  



def guardarMat(request):
    if 'idMateria' in request.POST and 'nombre' in request.POST and 'descripcion' in request.POST:
        idMateria=request.POST['idMateria']
        nombre=request.POST['nombre']
        descripcion=request.POST['descripcion']
        p=models.datos(idMateria=idMateria,nombre=nombre,descripcion=descripcion)
        p.save()
        return render(request, 'consultaMa.html', {'msg' : 'Se registro correctamente..'})
    else:
        return render(request, 'registraMa.html', {'msg':'El registro no se pudo realizar'})

def consultaMat(request):
    registro= models.datos.objects.all()
    return render(request,'consultaMa.html',{"registro":registro})

def modificarMa(request):
    if 'idMateria' in request.POST and 'nombre' in request.POST and 'descripcion' in request.POST: 
      p =models.datos(idMateria= request.POST['idMateria'])
      p.nombre = request.POST['nombre']
      p.descripcion = request.POST['descripcion']
      p.save()
    return redirect('/consulta')

def editarMa(request):
    if 'idMateria' in request.POST:
     registro = models.datos.objects.get(idMateria=request.POST['idMateria'])
     return render(request, 'modificarMa.html',{"reg":registro})
    else:
     return redirect('/consulta')
       