from django.db import models
from django.core.exceptions import ValidationError


class Conductor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    fecha_nac = models.DateField(null=False)

    def __str__(self):
        return self.rut


class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=6, unique=True)
    marca = models.CharField(max_length=50, null=False)
    modelo = models.CharField(max_length=50, null=False)
    year = models.DateField(null=False)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)

    def __str__(self):
        return self.marca


class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=10, null=False)
    numero = models.CharField(max_length=10, null=False)
    dpto = models.CharField(max_length=10, null=False)
    comuna = models.CharField(max_length=50, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=50, null=False)
    conductor_id = models.OneToOneField(Conductor, on_delete=models.CASCADE)
