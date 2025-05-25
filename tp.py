#  1. Clase Perro ● Atributos: nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado ('disponible', 'reservado', 'adoptado'), temperamento, id.
# ● Métodos: cambiar estado, mostrar información, etc.

class Perro(object):
    def __init__(self, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado, temperamento, id):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado
        self.temperamento = temperamento
        self.id = id
        
    def cambiar_estado(self, estado):
        self.estado = estado
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso}")
        print(f"Estado salud: {self.estado_salud}")
        print(f"Vacunado: {self.vacunado}")
        print(f"Estado: {self.estado}")
        print(f"Temperamento: {self.temperamento}")
        print(f"ID: {self.id}")
   
#2. Clase UsuarioAdoptante
#● Atributos: nombre, dni, email, preferencias (raza, edad, tamaño),historial_adopciones.
#● Métodos: registrarse, modificar datos, ver historial, etc.

class UsuarioAdoptante(object):
    def __init__(self, nombre, dni, email, raza, edad, tamaño, historial_adopciones):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.edad = edad
        self.raza = raza
        self.tamaño = tamaño
        self.historial_adopciones = historial_adopciones
        
    def registrarse(self, registrarse):
        self.registrarse = registrarse
        
    def modificar_datos(self, modificar_datos):
        self.modificar_datos = modificar_datos
        
    def ver_historial(self, ver_historial):
        self.ver_historial = ver_historial  
   

#🔁 3. Clase SistemaAdopcion ● Métodos para: ○ Cargar y eliminar perros ○ Registrar usuarios ○ Postular a un perro ○ Confirmar adopción ○ Sugerir perros según preferencias
# ○ Mostrar listados (perros disponibles, por estado, por usuario)
