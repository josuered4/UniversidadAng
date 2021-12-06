from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from .forms import CustomAuthenticationForm


# Create your views here.
def home(request):
   # Creamos el formulario de autenticación vacío
    form = CustomAuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = CustomAuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/autenticacion')

    # Si llegamos al final renderizamos el formulario
    return render(request, "core/index.html", {'form': form})




