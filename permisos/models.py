from django.db import models

# Create your models here.

class Tipo(models.Model):
    tipo_ausencia = models.CharField(max_length=100)

class Empleado(models.Model):
    cedula = models.CharField(max_length=20)
	apellido = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)
    

class Permiso(models.Model):
    tipo_permiso = models.ForeignKey(Tipo)
	empleado = models.ForeignKey(Empleado)
    fecha_desde = models.DateTimeField('date published')
	fecha_hasta = models.DateTimeField('date published')
    numero_dias = models.IntegerField(default=0)
