from django.shortcuts import render, redirect
from BBDD.models import Carrera
from .forms import CarreraForm

# Create your views here.

def Carreras(request):
    if request.user.is_authenticated:
        Carreras = Carrera.objects.all()
        Datos = {
            'Carreras':Carreras
            }
        return render(request, "Carreras/carreras.html",Datos)
    return redirect('/')
    

def añadirCarrera(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = CarreraForm()
            Carreras = Carrera.objects.all()
            contexto = {
                'form':form,
                'Carreras':Carreras,
            }
            if form.is_valid():
                form.save()
                return render(request,'Carreras/añadirCarrera.html',contexto)
        else:
            form = CarreraForm(request.POST)
            Carreras = Carrera.objects.all()
            contexto = {
                'form':form,
                'Carreras':Carreras,
            }
            if form.is_valid():
                form.save()
                return render(request,'Carreras/añadirCarrera.html',contexto)
        return render(request,'Carreras/añadirCarrera.html',contexto)
    return redirect('/')




def editarCarrera(request, pk):
    carrera = Carrera.objects.get(pk = pk)
    Carreras = Carrera.objects.all()
    if request.method == 'GET': 
        form = CarreraForm(instance = carrera)
        context = {
            'form':form,
            'Carreras':Carreras,
        }
        if form.is_valid():
            form.save()
            return render(request,'Carreras/añadirCarrera.html', context)
    else:
        form = CarreraForm(request.POST, instance= carrera)
        context = {
            'form':form,
            'Carreras':Carreras,
        }
        if form.is_valid():
            form.save()
            return render(request,'Carreras/añadirCarrera.html', context) 
    return render(request,'Carreras/añadirCarrera.html',context)


def delCarrera(request, pk):
    carrera = Carrera.objects.get(pk = pk)
    carrera.delete()
    return redirect('/addcarreras')