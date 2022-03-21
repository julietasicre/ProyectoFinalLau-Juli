from django import forms

# required=False 

class GerenteFormulario(forms.Form):
    nombre= forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=20)
    dni= forms.IntegerField()
    email= forms.EmailField()

class GerenteBusqueda (forms.Form):
    nombre= forms.CharField(max_length=20)
