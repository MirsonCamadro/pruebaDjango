from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib.auth.decorators import login_required, permission_required



def index(request):
    return render(request, 'vehiculo/index.html')

@login_required
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})


@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.rango_precio = 'Bajo'
        elif vehiculo.precio <= 30000:
            vehiculo.rango_precio = 'Medio'
        else:
            vehiculo.rango_precio = 'Alto'
    return render(request, 'vehiculo/listar_vehiculos.html', {'vehiculos': vehiculos})

