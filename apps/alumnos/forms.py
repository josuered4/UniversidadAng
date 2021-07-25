#Para la creacion de formulario, se crea una clase y ya solo se manda a llamar en una vista como si 
#fuera un modelo 

from django import forms 
from BBDD.models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
