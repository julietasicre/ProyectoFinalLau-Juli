from django import forms

class GerenteFormulario(forms.Form):
    nombre= forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=20)
    dni= forms.IntegerField()
    email= forms.EmailField()