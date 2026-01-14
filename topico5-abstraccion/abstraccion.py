# abstraccion: hacer visible lo importante y ocultar lo irrelevante

class Cafetera:
    def hacer_cafe(self):
        self._calentar_agua()
        self._moler_cafe()
        self._mezclar()
        print("☕ Tu café está listo")

    # Métodos internos (detalles ocultos)
    def _calentar_agua(self):
        print("Calentando agua...")

    def _moler_cafe(self):
        print("Moliendo granos de café...")

    def _mezclar(self):
        print("Mezclando agua con café...")


cafetera = Cafetera()
cafetera.hacer_cafe() # Solo interactúas con este método, no con los detalles internos


class RepositorioUsuarios:
    def guardar_usuario(self, nombre: str):
        # El usuario de la clase no sabe si esto va a SQL, NoSQL, archivo, etc.
        self._conectar()
        self._insertar(nombre)
        self._cerrar_conexion()

    def _conectar(self):
        print("Conectando a la base de datos...")

    def _insertar(self, nombre):
        print(f"Insertando usuario {nombre}...")

    def _cerrar_conexion(self):
        print("Cerrando conexión...")


repo = RepositorioUsuarios()
repo.guardar_usuario("Pedro")


####### Clases abstractas
# * No se puede instanciar directamente.
# * Sirve como plantilla para otras clases.
# * Obliga a que las clases hijas implementen ciertos métodos.
# * asegura polimorfismo

# Ejemplo típico:
# Repositorios (UserRepository, FileUserRepository, PostgresUserRepository)
# Pasarelas de pago (StripePayment, PaypalPayment)
# Notificaciones (EmailNotification, SMSNotification)
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def moverse(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

    def moverse(self):
        return "El perro corre"


class Pajaro(Animal):
    def hacer_sonido(self):
        return "Pío"

    def moverse(self):
        return "El pájaro vuela"

perro = Perro()
print(perro.hacer_sonido())
print(perro.moverse())

pajaro = Pajaro()
print(pajaro.hacer_sonido())
print(pajaro.moverse())
