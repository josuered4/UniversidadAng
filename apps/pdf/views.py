from django.shortcuts import render
from BBDD.models import Alumno, TipoPago

# Create your views here.
#html2pdf imports
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from datetime import datetime


def imprimePdf(request, pk, type_Pago):
            pk = pk
            type_Pago = type_Pago
            alumno = Alumno.objects.get(pk = pk)
            pago = TipoPago.objects.get(pk = type_Pago)
            date = datetime.today()
            template = get_template('baucher/recibo.html')
            context = {
                'comp': {'name': 'Universidad Los Angeles', 'ruc': 'clave', 'address':'Direccion'},
                'Alumno':alumno,
                'Pagos': pago,
                'fecha':date
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf',)
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                    html, dest=response)
            return response



def imprimePdfAdicional(request, pk, nombre):
            pk = pk
            nombre = nombre
            alumno = Alumno.objects.get(pk = pk)
            pago = TipoPago.objects.filter(Nombre = nombre).filter(Historial=pk)
            template = get_template('baucher/recibo1.html')
            context = {
                'comp': {'name': 'Universidad Los Angeles', 'ruc': 'clave', 'address':'Direccion'},
                'Alumno':alumno,
                'Pagos': pago
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf',)
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisa_status = pisa.CreatePDF(
                    html, dest=response)
            return response


