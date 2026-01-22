# ISP interface segregation principle
# no obligar a una clase implementar metodos que no necesita
# Una interfaz debe representar un “ROL”, no un “OBJETO REAL”.
from abc import ABC, abstractmethod


class Vehiculo(ABC):
    @abstractmethod
    def conducir(self):
        pass

    @abstractmethod
    def volar(self):
        pass

    @abstractmethod
    def navegar(self):
        pass


class Auto(Vehiculo):
    def conducir(self):
        print("Conduciendo")

    def volar(self):
        raise NotImplementedError()

    def navegar(self):
        raise NotImplementedError()


# ######################### Solucion  #########################
class Conducible1(ABC):
    @abstractmethod
    def conducir(self):
        pass


class Volable1(ABC):
    @abstractmethod
    def volar(self):
        pass


class Navegable1(ABC):
    @abstractmethod
    def navegar(self):
        pass


class Auto1(Conducible1):
    def conducir(self):
        print("Auto conduciendo")


class Avion1(Conducible1, Volable1):
    def conducir(self):
        print("Rodando por pista")

    def volar(self):
        print("Avión volando")


class Barco1(Navegable1):
    def navegar(self):
        print("Barco navegando")
