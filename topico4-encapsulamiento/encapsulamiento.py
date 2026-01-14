from dataclasses import dataclass


class Persona:
    def __init__(self, nombre: str, contrasenia: str):
        self._nombre = nombre
        self.__contrasenia = contrasenia  # ojo no se usa mucho, rompe: dataclass, herencia, testing

    def get_nombre(self):
        return self._nombre

    def get_contrasenia(self):
        return self.__contrasenia

    def set_contrasenia(self, new_contrasenia: str):
        self.__contrasenia = new_contrasenia


per = Persona("Juan", "contraseña")
print(per.get_nombre())
print(per.get_contrasenia())

per.set_contrasenia("nueva_contraseña")
print(per.get_contrasenia())
print('--------------------1-------------------------')
# decorador
def decorador(funct):
    def funcion_modificada():
        print("Antes de la función")
        funct()
        print("Después de la función")
    return funcion_modificada


def saludo():
    print("hola")


saludo_modificado = decorador(saludo)
saludo_modificado()


@decorador
def despedida():
    print("adiós")
despedida()
print('--------------------2-------------------------')

######### Encapsulamiento “moderno” en Python: @property
# * Accedes como si fuera un atributo
# * Internamente sigue estando protegido
# * Puedes validar sin cambiar cómo se usa desde afuera
class Persona1:
    def __init__(self, nombre: str, contrasenia: str):
        self._nombre = nombre
        self.__contrasenia = contrasenia

    @property
    def nombre(self):
        return self._nombre

    @property
    def contrasenia(self):
        return self.__contrasenia

    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia: str):
        if len(nueva_contrasenia) < 6: # permite validaciones
            raise ValueError("La contraseña debe tener al menos 6 caracteres")
        self.__contrasenia = nueva_contrasenia


per1 = Persona1("Juan", "contraseña123")

print(per1.nombre)
print(per1.contrasenia)

per1.contrasenia = "nueva123" # se accese como atributo y permite validacion
print(per1.contrasenia)


###### dataclasses: se usa cuando tienes muchas clases de datos

@dataclass
class Persona2:
    nombre: str
    _contrasenia: str

    @property
    def contrasenia(self):
        return self.__contrasenia

    @contrasenia.setter
    def contrasenia(self, value: str):
        if len(value) < 8:
            raise ValueError("Contraseña muy corta")
        self.__contrasenia = value


class ServicioUsuarios:
    def crear_usuario(self, nombre, password):
        self.__validar_password(password)
        self.__guardar_en_db(nombre, password)

    def __validar_password(self, password):
        ...

    def __guardar_en_db(self, nombre, password):
        ...
