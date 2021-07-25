from django.contrib import admin
from .models import Carrera, Alumno, TipoPago, HistPago 
# Register your models here.

admin.site.register(Carrera)
admin.site.register(Alumno)
admin.site.register(TipoPago)
admin.site.register(HistPago)
