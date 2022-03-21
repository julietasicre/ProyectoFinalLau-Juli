from django.db import models

class gerente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    dni= models.IntegerField()
    email= models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class reponedor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    dni= models.IntegerField()
    email= models.EmailField()
    desempeño= models.BooleanField()

class cajero(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    dni= models.IntegerField()
    email= models.EmailField()
    desempeño= models.BooleanField()
