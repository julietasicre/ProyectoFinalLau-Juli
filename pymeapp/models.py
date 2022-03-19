from django.db import models

class cliente(models.Model):
    numero=models.IntegerField()
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    email=models.EmailField()

class articulo(models.Model):
    producto=models.IntegerField()
    seccion=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)

class envio(models.Model):
    fecha=models.DateField()
    cantidad= models.IntegerField()
    direccion= models.CharField(max_length=50)
    entregado = models.BooleanField()
