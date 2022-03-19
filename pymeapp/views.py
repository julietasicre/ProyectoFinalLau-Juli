from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def pymeapp(request):
    return HttpResponse('<h1> Bienvenidos a nuestra app online </h1>')

def plantilla(request):
    template = loader.get_template('plantilla.html')
    datos= {
        'lista': ["primero","segundo","tercero"]
    }
    plantilla_generada = template.render(datos)
    return HttpResponse (plantilla_generada) 


