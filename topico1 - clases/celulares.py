from dataclasses import dataclass, asdict


class Celular:
    # atributo de clase
    # Todos los objetos comparten el mismo valor.
    marca = "samsung"
    modelo = "S3"


class Celular1:
    def __init__(self, marca, modelo):
        # atributos de instancia
        # Cada objeto tiene sus propios valores
        self.marca = marca
        self.modelo = modelo


class Celular2:
    def __init__(dog, marca, modelo):
        dog.marca = marca
        dog.modelo = modelo


class Celular3:
    chip = "Theros"

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


# TYPE HINTS, no validan datos en tiempo de ejecucion, programa se ejecuta
# No es para el intérprete. Es para TI, tu editor y tus herramientas.
# * autocompletado inteligente, el editor sabe que modelo es "str" y te sugiere metodos
# * ayuda a pylance detectar errores
# * fastApi, pydantic(mas usado) si usan tipos para validar datos

# DATACLASS
# genera automaticamente:
# * __init__, __repr__, comparaciones
# ¿Esta clase existe para representar datos? Sí → @dataclass, No → clase normal
# 1. estructura de datos, solo guarda datos
@dataclass
class Punto:
    x: float
    y: float

# 2. modelo de dominio
# 3. DTOs, Esquemas, Configuraciones


@dataclass
class CrearUsuarioDTO:
    nombre: str
    email: str
    password: str


usuario = CrearUsuarioDTO("Juan", "juan@mail.com", "123") # serializacion: convertir dict -> json
print(asdict(usuario))
# {'nombre': 'Juan', 'email': 'juan@mail.com', 'password': '123'}


@dataclass
class Celular4:
    marca: str
    modelo: str

# como funciona internamente __init__ junto con selft
# Celular1.__init__(cel1, "samsung", "s23")
# Celular1.__init__(cel2, "xioamin", "F45")
