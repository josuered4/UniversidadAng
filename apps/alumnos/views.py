from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import logout as do_logout
from BBDD.models import Alumno
from .forms import AlumnoForm



####
# Create your views here.
def autenticacion(request):
   #Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        alumno = Alumno.objects.all()
        context = {
            'alumnos':alumno
        }
    
        return render(request, "alumnos/index.html", context)    
    # En otro caso redireccionamos al login
    return redirect('/')


    


def AddAlumno(request):
    if request.user.is_authenticated:
        if request.method == 'POST':#Se comprueba si el fomulario envia inf por el metod post
            form = AlumnoForm(request.POST)#Se crea un objeto mas lo que se obtuno con el post
            if form.is_valid():#Se comprueba si el fomuario es valio
                form.save()#Se guarda la 
                return redirect("/autenticacion")    
        else:
            form = AlumnoForm()#se crea un formulario separado   
            return render(request, "alumnos/addAlumno.html", {'form':form, 'accion':'Añadir'})
    return redirect('/')


def editAlumnos(request, pk):#Edicion de alumnos, se pide la llave primaria 
    alumno = Alumno.objects.get(pk = pk) # se obtiene el valor de pk y se le asigna a otra varible del mismo nombre
    if request.method == 'GET':
        form = AlumnoForm(instance = alumno)
    else:
        form = AlumnoForm(request.POST, instance = alumno) # se toma el fomulario con las modificaciones
        if form.is_valid():#se verifica si es valido 
            form.save()#se guarde el formulario
            return redirect("/autenticacion")#se redirecciona una ves guardado el formulario
    return render (request, "alumnos/addAlumno.html", {'form':form, 'accion':'Editar'}) # se envian datos al template




def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
    
