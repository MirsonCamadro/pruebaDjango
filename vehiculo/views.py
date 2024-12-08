from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

def index(request):
    return render(request, 'vehiculo/index.html')  # Correcta ruta a la plantilla

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})  # Correcta ruta a la plantilla

def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehiculos': vehiculos})
