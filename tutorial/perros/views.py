from django.shortcuts import render, redirect, get_object_or_404
from .models import Perro, UsuarioAdoptante
from .forms import UsuarioAdoptanteForm

def home(request):
    return render(request, 'perros/home.html')

def listar_perros(request):
    perros = Perro.objects.filter(estado="disponible")
    return render(request, 'perros/listar_perros.html', {'perros': perros})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioAdoptanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_perros')
    else:
        form = UsuarioAdoptanteForm()
    return render(request, 'perros/registrar_usuario.html', {'form': form})

def adoptar_perro(request, perro_id):
    perro = get_object_or_404(Perro, id=perro_id)
    if request.method == 'POST':
        dni = request.POST.get('dni')
        try:
            usuario = UsuarioAdoptante.objects.get(dni=dni)
        except UsuarioAdoptante.DoesNotExist:
            return render(request, 'perros/adoptar_perro.html', {
                'perro': perro,
                'error': 'Usuario no registrado. Primero debés registrarte.'
            })

        if perro.estado == 'disponible':
            perro.estado = 'reservado'
            perro.save()
            usuario.historial_adopciones.add(perro)
            return render(request, 'perros/adopcion_confirmada.html', {'perro': perro, 'usuario': usuario})

    return render(request, 'perros/adoptar_perro.html', {'perro': perro})