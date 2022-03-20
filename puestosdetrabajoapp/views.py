from django.shortcuts import render
from .forms import GerenteFormulario

def crear_gerente(request):
    form = GerenteFormulario
    return render(request, 'puestosdetrabajoapp/crear_gerente.html', {'form': form})
