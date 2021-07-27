from django.shortcuts import render, redirect
from BBDD.models import TipoPago
from .forms import PagosForm
# Create your views here.

def Pagos(request):
    if request.user.is_authenticated:
        pagos = TipoPago.objects.all()
        Context = {
            'pagos':pagos
            }
        return render(request, "Pagos/pagos.html", Context)
    return redirect('/home')


def addPago(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PagosForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/pagos")    
        else:
            form = PagosForm()#se crea un formulario separado   
            return render(request, "Pagos/addpago.html", {'form':form, 'accion':'Añadir'})
    return redirect('/home')


def editpago(request, pk):#Edicion de alumnos, se pide la llave primaria 
    pago = TipoPago.objects.get(pk = pk) # se obtiene el valor de pk y se le asigna a otra varible del mismo nombre
    if request.method == 'GET':
        form = PagosForm(instance = pago)
    else:
        form = PagosForm(request.POST, instance = pago) # se toma el fomulario con las modificaciones
        if form.is_valid():#se verifica si es valido 
            form.save()#se guarde el formulario
            return redirect("/pagos")#se redirecciona una ves guardado el formulario
    return render (request, "Pagos/addpago.html", {'form':form, 'accion':'Editar'}) 


