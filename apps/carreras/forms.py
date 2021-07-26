from django import forms 
from BBDD.models import Carrera

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'
        