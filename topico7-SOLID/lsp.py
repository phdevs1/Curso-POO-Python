# LSP:
from abc import ABC, abstractmethod


class Rectangulo:
    def set_ancho(self, ancho):
        self.ancho = ancho

    def set_alto(self, alto):
        self.alto = alto

    def area(self):
        return self.ancho * self.alto


class Cuadrado(Rectangulo):
    def set_ancho(self, ancho):
        self.ancho = ancho

    def set_alto(self, alto):
        self.alto = alto


def imprimir_area(rectangulo: Rectangulo):
    rectangulo.set_ancho(4)
    rectangulo.set_alto(5)
    print(rectangulo.area())


r = Rectangulo()
imprimir_area(r)

c = Cuadrado()
imprimir_area(c)


# ######################### Solucion  #########################
class Figura(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass


class Rectangulo1(Figura):
    def __init__(self) -> None:
        self._ancho: float = 0
        self._alto: float = 0

    def set_ancho(self, ancho: float) -> None:
        self._ancho = ancho

    def set_alto(self, alto: float) -> None:
        self._alto = alto

    def get_area(self) -> float:
        return self._alto * self._ancho


class Cuadrado2(Figura):
    def __init__(self) -> None:
        self._lado: float = 0

    def set_lado(self, lado: float) -> None:
        self._lado = lado

    def get_area(self) -> float:
        return self._lado * self._lado


def imprimir_area2(figura: Figura):

    print(figura.get_area())


r1 = Rectangulo1()
r1.set_alto(4)
r1.set_ancho(5)
imprimir_area2(r1)

c2 = Cuadrado2()
c2.set_lado(4)
imprimir_area2(c2)


# ######################### caso 2  #########################
class Vehiculo:
    def velocidad_maxima(self):
        return 200


class AutoPlastico(Vehiculo):
    def velocidad_maxima(self):
        raise Exception("auto no tiene velocidad max")


def imprimir_velocidad(vehiculo: Vehiculo):
    try:
        print(vehiculo.velocidad_maxima())
    except Exception:
        print("algo fallo")


print("------------------caso 2---------------------")
v1 = Vehiculo()
imprimir_velocidad(v1)

v2 = AutoPlastico()
imprimir_velocidad(v2)


# ######################### Solucion  #########################
class Articulo(ABC):
    @abstractmethod
    def descripcion(self) -> str:
        pass


class Vehiculo2(Articulo):
    @abstractmethod
    def velocidad_maxima(self) -> int:
        pass

    def descripcion(self) -> str:
        return f"Vehículo con velocidad máxima de {self.velocidad_maxima()} km/h"


class Auto2(Vehiculo2):
    def __init__(self, velocidad: int):
        self._velocidad = velocidad

    def velocidad_maxima(self) -> int:
        return self._velocidad


class Juguete2(Articulo):
    def __init__(self, nombre: str):
        self._nombre = nombre

    def descripcion(self) -> str:
        return f"Juguete: {self._nombre}"


class AutoPlastico2(Juguete2):
    def __init__(self):
        super().__init__("Auto de plástico")


def imprimir_velocidad2(vehiculo: Vehiculo2):
    print(f"Velocidad máxima: {vehiculo.velocidad_maxima()} km/h")


def mostrar_articulo(articulo: Articulo):
    print(articulo.descripcion())


print("------------------Solución ---------------------")
auto_real = Auto2(200)
auto_juguete = AutoPlastico2()

imprimir_velocidad2(auto_real)  # Velocidad máxima: 200 km/h


# Pero todos pueden mostrarse como artículos
mostrar_articulo(auto_real)  # Vehículo con velocidad máxima de 200 km/h
mostrar_articulo(auto_juguete)  # Juguete: Auto de plástico


# class SinVelocidadMaxima(Exception):
#     pass


# class Vehiculo:
#     def velocidad_maxima(self):
#         return 200


# class AutoPlastico(Vehiculo):
#     def velocidad_maxima(self):
#         raise SinVelocidadMaxima("auto sin velocidad maxima")


# class Auto(Vehiculo):
#     def velocidad_maxima(self):
#         return 1 / 0  # BUG


# def imprimir_velocidad(vehiculo: Vehiculo):
#     try:
#         print(vehiculo.velocidad_maxima())
#     except SinVelocidadMaxima as e:
#         print(f"error: {e}")


# print("------------------caso 2---------------------")
# v1 = Vehiculo()
# imprimir_velocidad(v1)

# v2 = AutoPlastico()
# imprimir_velocidad(v2)

# v3 = Auto()
# try:
#     imprimir_velocidad(v3)
# except Exception as e:
#     print(f"error: {e}")
#     raise
