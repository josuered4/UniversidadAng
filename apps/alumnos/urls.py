from django.urls import path
from . import views



urlpatterns = [
    path('logout/', views.logout),
    path('autenticacion/', views.autenticacion, name='autenticacion'),
    path('addAlumno/', views.AddAlumno, name = 'addAlumno'),
    path('editAlumno/<int:pk>/', views.editAlumnos, name = 'editAlumno')

]

