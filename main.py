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

class SistemaAdopcion:
    def __init__(self):
        self.perros = []
        self.usuarios = []

    def cargar_perro(self, nuevo_perro):
        self.perros.append(nuevo_perro)
        print(f"Perro cargado: {nuevo_perro.nombre}")

    def eliminar_perro(self, id_perro):
        for perro in self.perros:
            if perro.id == id_perro:
                self.perros.remove(perro)
                print(f"Perro eliminado: {perro.nombre}")
                return
        print("Perro no encontrado.")

    def registrar_usuario(self, nuevo_usuario):
        self.usuarios.append(nuevo_usuario)
        print(f"Usuario registrado: {nuevo_usuario.nombre}")

    def postular_perro(self, id_perro):
        for perro in self.perros:
            if perro.id == id_perro:
                if perro.estado == "disponible":
                    perro.cambiarEstado("reservado")
                    print(f"Perro {perro.nombre} reservado con éxito.")
                    return perro
                else:
                    print(f"El perro {perro.nombre} no está disponible.")
                    return None
        print("No se encontró el perro con ese ID.")
        return None

    def confirmar_adopcion(self, id_perro, dni_usuario):
        perro_encontrado = None
        usuario_encontrado = None

        for perro in self.perros:
            if perro.id == id_perro and perro.estado == "reservado":
                perro.cambiarEstado("adoptado")
                perro_encontrado = perro
                break

        if perro_encontrado is None:
            raise ValueError("Perro no encontrado o no reservado.")

        for usuario in self.usuarios:
            if usuario.dni == dni_usuario:
                usuario_encontrado = usuario
                break

        if usuario_encontrado is None:
            raise ValueError("Usuario no encontrado.")

        usuario_encontrado.historial_adopciones.append(perro_encontrado)
        print(f"Adopción confirmada: {perro_encontrado.nombre} fue adoptado por {usuario_encontrado.nombre}.")

    def sugerir_perros(self, dni_usuario):
        usuario = next((u for u in self.usuarios if u.dni == dni_usuario), None)

        if not usuario:
            print("Usuario no encontrado.")
            return

        sugerencias = [
            perro for perro in self.perros
            if perro.estado == "disponible" and
               perro.raza == usuario.preferencias.get("raza") and
               perro.edad == usuario.preferencias.get("edad") and
               perro.tamaño == usuario.preferencias.get("tamaño")
        ]

        if sugerencias:
            print(f"Perros sugeridos para {usuario.nombre}:")
            for p in sugerencias:
                print(f"- {p.nombre} (ID: {p.id})")
        else:
            print("No se encontraron perros que coincidan con las preferencias.")

    def mostrar_perros_disponibles(self):
        disponibles = [p for p in self.perros if p.estado == "disponible"]
        if disponibles:
            print("Perros disponibles:")
            for p in disponibles:
                print(f"- {p.nombre} (ID: {p.id}, Raza: {p.raza}, Edad: {p.edad})")
        else:
            print("No hay perros disponibles.")

    def mostrar_perros_por_estado(self, estado):
        filtrados = [p for p in self.perros if p.estado == estado]
        if filtrados:
            print(f"Perros con estado '{estado}':")
            for p in filtrados:
                print(f"- {p.nombre} (ID: {p.id})")
        else:
            print(f"No hay perros con estado '{estado}'.")

    def mostrar_historial_usuario(self, dni_usuario):
        usuario = next((u for u in self.usuarios if u.dni == dni_usuario), None)
        if usuario:
            print(f"Historial de adopciones de {usuario.nombre}:")
            usuario.ver_historial()
        else:
            print("Usuario no encontrado.")