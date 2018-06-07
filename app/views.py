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

def nombre(request):
    valores= range(10)
    p = persona.Persona()
    p.iniciar(1,'Josue')
    p2= persona.Persona()
    p2.iniciar(2,'Jesus')

    personas= [p,p2]
    return render(request,'nombre.html',{'personas':personas})

def esclava(request):
    return render(request, 'esclavo.html')    

def sumar(request):
    if 'num1' in request.POST and 'num2' in request.POST:
     n1=request.POST['num1']
     n2=request.POST['num2']
     if len(n1)<=0 and len(n2)<=0:
         return render(request,'esclavo.html')
     suma= int(n1)+ int(n2)
     return render(request, 'esclavo.html',{'suma':suma, 'num1':n1, 'num2':n2})
    else:
        return render(request,'esclavo.html')
     

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
     p= models.Alumn(idAlumno= idAlumno,nombre = nombre, carrera = carrera, correo=correo, numero=numero, contraseña=contraseña)
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




       