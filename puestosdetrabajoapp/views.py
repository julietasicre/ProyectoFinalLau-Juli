from django.shortcuts import render, redirect
from .models import gerente
from .forms import GerenteFormulario , GerenteBusqueda

def crear_gerente(request):
    if request.method == 'POST':
        form = GerenteFormulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Gerente = gerente (nombre = data['nombre'],apellido=data['apellido'], dni=data['dni'], email=data['email'])
            Gerente.save()
            return render(request, 'pymeapp/platilla.html', {})
            # return redirect("pymeapp")

    form = GerenteFormulario
    return render(request, 'puestosdetrabajoapp/crear_gerente.html', {'form': form})

def lista_gerentes (request):
    nombre_a_buscar = request.GET.get('nombre',None)
    if nombre_a_buscar is not None:
        Gerentes = gerente.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        Gerentes = gerente.objects.all()

    form= GerenteBusqueda()
    return render(request, 'puestosdetrabajoapp/lista_gerentes.html', {'form': form, 'Gerentes': Gerentes})