# single responsability principle: una clase solo tiene una razon para cambiar
class Auto:
    def __init__(self):
        self.posicion = 0
        self.combustible = 100

    def mover(self, distancia):
        if self.combustible >= distancia * 0.5:
            self.posicion += distancia
            self.combustible -= distancia * 0.5
        else:
            print("No hay suficiente combustible para mover esa distancia.")

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible


