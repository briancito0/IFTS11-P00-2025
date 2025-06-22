import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from perros.models import Perro, UsuarioAdoptante


def crear_perro():
    perro, creado = Perro.objects.get_or_create(
        nombre='Luna',
        raza='Labrador',
        edad=2,
        tamaño='Mediano',
        peso=22.5,
        estado_salud='Excelente',
        vacunado=True,
        estado='disponible',
        temperamento='Juguetón'
    )
    if creado:
        print(f"Perro {perro.nombre} creado.")
    else:
        print(f"Perro {perro.nombre} ya existe.")
    return perro


def crear_usuario():
    usuario, creado = UsuarioAdoptante.objects.get_or_create(
        dni='12345678',
        defaults={
            'nombre': 'Carlos López',
            'email': 'carlos@example.com',
            'raza_preferida': 'Labrador',
            'edad_preferida': 2,
            'tamaño_preferido': 'Mediano'
        }
    )
    if creado:
        print(f"Usuario {usuario.nombre} creado.")
    else:
        print(f"Usuario {usuario.nombre} ya existe.")
    return usuario


def postular(perro, usuario):
    if perro.estado != 'disponible':
        print(f"El perro {perro.nombre} no está disponible.")
        return
    perro.estado = 'reservado'
    perro.save()
    print(f"Perro {perro.nombre} reservado para {usuario.nombre}.")

def confirmar(perro, usuario):
    if perro.estado != 'reservado':
        print(f"El perro {perro.nombre} no está reservado.")
        return
    perro.estado = 'adoptado'
    perro.save()
    usuario.historial_adopciones.add(perro)
    print(f"{usuario.nombre} adoptó a {perro.nombre}.")

if __name__ == '__main__':
    perro = crear_perro()
    usuario = crear_usuario()
    postular(perro, usuario)
    confirmar(perro, usuario)