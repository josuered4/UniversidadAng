from django.urls import path
from . import views


urlpatterns = [
    path('imprimePdf/<int:pk>/<int:type_Pago>', views.imprimePdf,name = 'imprimePdf'),
    #path('PagoAdicional/', views.PagoAdicional, name = 'PagoAdicional'),
    path('imprimePdfAdicional/<int:pk>/<str:nombre>', views.imprimePdfAdicional,name = 'imprimePdfAdicional'),
]