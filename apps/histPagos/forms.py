from django import forms
from django.forms.forms import Form 
from BBDD.models import HistPago

class HistPagoForm(forms.ModelForm):
    class Meta:
        model = HistPago
        fields = '__all__'


class Busqueda(forms.Form):
    matricula = forms.CharField(max_length = 150)