from django.db import models

class Perro(models.Model):
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
        ('adoptado', 'Adoptado'),
    ]

    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('H', 'Hembra'),
    ]

    TAMANO_CHOICES = [
        ('S', 'Pequeño'),
        ('M', 'Mediano'),
        ('L', 'Grande'),
        ('X', 'Extra Grande'),
    ]

    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    edad = models.IntegerField()
    tamaño = models.CharField(max_length=1, choices=TAMANO_CHOICES)
    peso = models.FloatField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    estado_salud = models.CharField(max_length=100)
    vacunado = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
    temperamento = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.estado})"


class UsuarioAdoptante(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    raza_preferida = models.CharField(max_length=100)
    edad_preferida = models.IntegerField()
    tamaño_preferido = models.CharField(max_length=1, choices=Perro.TAMANO_CHOICES)

    historial_adopciones = models.ManyToManyField(Perro, blank=True)

    def __str__(self):
        return self.nombre