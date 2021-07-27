from django.urls import path, re_path
from . import views


urlpatterns = [
    path('carreras/', views.Carreras, name='carreras'),
    path('addcarreras/', views.añadirCarrera, name='addcarreras'),
    path('editcarreras/<int:pk>/', views.editarCarrera, name='editcarreras'),
    path('deletecarrera/<int:pk>/',views.delCarrera,name = 'delCarrera'),
    
]