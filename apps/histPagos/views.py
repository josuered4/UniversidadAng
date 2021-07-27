from django.shortcuts import render, redirect
from BBDD.models import HistPago
from .forms import HistPagoForm
from BBDD.models import Alumno

# Create your views here.

def registroPagos(request, matricula):
    if request.user.is_authenticated:
        HistPago.alumno = Alumno.objects.get(Matricula = matricula)#se transforma una variable legible el foreginkey
        registro = HistPago.objects.filter(Alumno = HistPago.alumno)
        context = {
            'pagos':registro,
            'matricula':matricula
            }
        return render(request, "histPagos/registrosPagos.html", context)
    return redirect('/home')


def addRegisPago(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = HistPagoForm(request.POST)
            if form.is_valid():
                form.save()
                matricula = form['Alumno']
                matricula = matricula.value()
                Alumnos = Alumno.objects.get(id = matricula)
                matricula = Alumnos.Matricula
                HistPago.alumno = Alumno.objects.get(Matricula = matricula)
                
                return redirect("histpagos", HistPago.alumno)    
        else:
            form = HistPagoForm()#se crea un formulario separado   
            return render(request, "histPagos/AddRegAlumno.html", {'form':form, 'accion':'Añadir'})
    return redirect('/home')


def editRegisPago(request, pk, matricula):#Edicion de alumnos, se pide la llave primaria 
    pago = HistPago.objects.get(pk = pk) # se obtiene el valor de pk y se le asigna a otra varible del mismo nombre
    if request.method == 'GET':
        form = HistPagoForm(instance = pago)
    else:
        form = HistPagoForm(request.POST, instance = pago) # se toma el fomulario con las modificaciones
        if form.is_valid():#se verifica si es valido 
            form.save()#se guarde el formulario
           
            matricula = matricula
            return redirect("histpagos",matricula)#se redirecciona una ves guardado el formulario

    return render (request, "histPagos/AddRegAlumno.html", {'form':form, 'accion':'Editar'}) 




