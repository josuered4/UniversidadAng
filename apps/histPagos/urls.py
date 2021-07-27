from django.urls import path, re_path
from . import views


urlpatterns = [
    path('histpagos/<int:matricula>/', views.registroPagos, name='histpagos'),
    path('addRegisPago/', views.addRegisPago, name='addRegisPago'),
    path('editRegisPago/<int:pk>/<int:matricula>/', views.editRegisPago, name='editRegisPago'),

    
]