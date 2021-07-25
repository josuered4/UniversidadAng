from django.db import models

# Create your models here.

class Carrera(models.Model):
    Nombre = models.CharField(max_length = 150)
    Cuatrimestral = models.BooleanField()
    NumCuatrimestres = models.IntegerField(default=0)
    Semestral = models.BooleanField()
    NumSemestres = models.IntegerField(default=0)

    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'




class Alumno(models.Model):
    Carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE) 
    Matricula = models.CharField(max_length = 150)
    Nombre = models.CharField(max_length = 150)
    ApellidoPaterno = models.CharField(max_length = 150)
    ApellidoMaterno = models.CharField(max_length = 150)
    Correo = models.EmailField()
    Telefono = models.CharField(max_length = 10)
    TipoPerido  = models.CharField(max_length = 150)
    

    def __str__(self):
        return self.Matricula


    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'




class TipoPago(models.Model):
    Nombre = models.CharField(max_length=50)
    Cantidad = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = 'TipoPago'
        verbose_name_plural = 'TipoPagos'




class HistPago(models.Model):
    Pago = models.OneToOneField(TipoPago, on_delete=models.CASCADE)
    Alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    Pagado = models.BooleanField()
    
    
    def __str__(self):
        return str(self.Pago)

    class Meta:
        verbose_name = 'HistPago'
        verbose_name_plural = 'HistPagos'
