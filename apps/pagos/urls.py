from django.urls import path, re_path
from . import views


urlpatterns = [
    path('pagos/', views.Pagos, name='pagos'),
    path('addpagos/', views.addPago, name='addpagos'),
    path('editpagos/<int:pk>/', views.editpago, name = 'editpagos')

    
    
]