from django.db import models

# Create your models here.

class ClsPasswords(models.Model):
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        varTexto = f'{self.id} {self.nombre}: ({self.descripcion})'
        return varTexto


    class Meta:
        db_table = 'Passwords'


class ClsPersonas(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apodo = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)

    nacimiento = models.DateField()

    feliz = models.BooleanField(blank=True)

    edad = models.IntegerField()
    dni = models.IntegerField()

    altura = models.FloatField()

    class Meta:
        db_table = 'Personas'


class ClsFacturas(models.Model):
    titular = models.CharField(max_length=50)
    direcion = models.CharField(max_length=50)
    fecha = None
    nroPedido = models.IntegerField()
    nroFactura = models.IntegerField()
    fechaVencimiento = None

    class Meta:
        db_table = 'Facturas'



class ClsDetalleFactura(models.Model):
    cantidad = models.IntegerField()
    producto = models.CharField(max_length=500)
    precioUnitario = models.FloatField()
    importe = models.FloatField()
    total = models.FloatField()

    class Meta:
        db_table = 'DetallesFactura'

