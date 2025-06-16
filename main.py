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

class CargarEliminarPerros:
    def __init__(self):
        self.perros = []
    
    def cargarPerro(self, nuevo_perro):
        self.perros.append(nuevo_perro)
        print(f"Perro cargado: {nuevo_perro.nombre}")
    
    def eliminarPerro(self, id_perro):
        for perro in self.perros:
            if perro.id == id_perro:
                self.perros.remove(perro)
                print(f"Perro eliminado: {perro.nombre}")
                return
        print("Perro no encontrado")

# Supongamos que ya tienes una clase Perro definida con atributos como id y nombre.
class Perro:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

# Crear una instancia de la clase CargarEliminarPerros
sistema = CargarEliminarPerros()

# Crear algunos perros
perro1 = Perro(1, "Max")
perro2 = Perro(2, "Luna")
perro3 = Perro(3, "Rocky")

# Probar el método cargarPerro
sistema.cargarPerro(perro1)  # Debería imprimir: "Perro cargado: Max"
sistema.cargarPerro(perro2)  # Debería imprimir: "Perro cargado: Luna"
sistema.cargarPerro(perro3)  # Debería imprimir: "Perro cargado: Rocky"

# Probar el método eliminarPerro
sistema.eliminarPerro(2)  # Debería imprimir: "Perro eliminado: Luna"
sistema.eliminarPerro(4)  # Debería imprimir: "Perro no encontrado"

# Verificar que los perros restantes están en la lista
for perro in sistema.perros:
    print(f"Perro en el sistema: {perro.nombre}")
    
    
    
class SistemaAdopcion:
    def __init__(self):
        self.perros = []
        self.usuarios = []

    def eliminarPerro(self, nombre):
        for perro in self.perros:
            if perro.nombre == nombre:
                self.perros.remove(perro)
                print(f"Perro {nombre} eliminado.")
                break
        else:
            print("No se encontró un perro con ese nombre.")
        print(f"{self.perros}")

    def registrarUsuario(self, nuevo_usuario):
        self.usuarios.append(nuevo_usuario)

    def postularPerro(self, id):
        for perro in self.perros:
            if perro.id == id:
                if perro.estado == "disponible":
                    perro.cambiarEstado("reservado")
                    print(f"Perro {id} reservado con éxito!")
                    return perro
                else:
                    print(f"Este perro {id} se encuentra reservado, no es posible postularse.")
                    return None
        print(f"No se encontró ningún perro con el ID {id}")
        return None

    def confirmarAdopcion(self, perro_id, usuario_dni):
        perro_encontrado = None
        usuario_encontrado = None

        for perro in self.perros:
            if perro.id == perro_id and perro.estado == "reservado":
                perro.cambiarEstado("adoptado")
                perro_encontrado = perro
                break

        if perro_encontrado is None:
            raise ValueError(f"No se encontró un perro reservado con ID {perro_id}.")

        for usuario in self.usuarios:
            if usuario.dni == usuario_dni:
                usuario_encontrado = usuario
                break

        if usuario_encontrado is None:
            raise ValueError(f"No se encontró un usuario con DNI {usuario_dni}.")

        usuario_encontrado.historial_adopciones.append(perro_encontrado)
        print(f"Adopción confirmada: {perro_encontrado.nombre} fue adoptado por {usuario_encontrado.nombre}")

    def sugerirPerro(self, dni):
        usuario_encontrado = None
        for usuario in self.usuarios:
            if usuario.dni == dni:
                usuario_encontrado = usuario
                break

        if not usuario_encontrado:
            print(f"No se encontró un usuario con DNI {dni}")
            return

        preferencias = usuario_encontrado.preferencias

        for perro in self.perros:
            if perro.estado == "disponible" and perro.raza == preferencias:
                print(f"Se sugiere el perro: {perro.nombre}")
    