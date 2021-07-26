from django.shortcuts import render
from BBDD.models import HistPago
from .forms import HistPagoForm

# Create your views here.

def registroPagos(request):
    if request.user.is_authenticated:
        registro = HistPago.objects.all()
        Context = {
            'pagos':registro
            }
        return render(request, "histPagos/registrosPagos.html", Context)
    return redirect('/home')


def addRegisPago(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = HistPagoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/histpagos")    
        else:
            form = HistPagoForm()#se crea un formulario separado   
            return render(request, "histPagos/AddRegAlumno.html", {'form':form, 'accion':'Añadir'})
    return redirect('/home')
