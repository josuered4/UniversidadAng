from django import forms 
from BBDD.models import HistPago

class HistPagoForm(forms.ModelForm):
    class Meta:
        model = HistPago
        fields = '__all__'