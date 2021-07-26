from django import forms 
from BBDD.models import TipoPago

class PagosForm(forms.ModelForm):
    class Meta:
        model = TipoPago
        fields = '__all__'
        