# single responsability principle: una clase solo tiene una razon para cambiar
class Auto:
    def __init__(self):
        self.posicion = 0
        self.combustible = 100

    def mover(self, distancia: int):
        if self.combustible >= distancia * 0.5:
            self.posicion += distancia
            self.combustible -= distancia * 0.5
        else:
            print("No hay suficiente combustible para mover esa distancia.")

    def agregar_combustible(self, cantidad: int):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible


auto1 = Auto()
auto1.mover(5)
print(auto1.obtener_combustible())


# ------------------------- opcion 1
class Auto2:
    def __init__(self, combustible) -> None:
        self.posicion = 0
        self.combustible = combustible

    def mover(self, distancia: int):
        if self.combustible.verificar_combustible(distancia):
            self.posicion += distancia
            self.combustible.reducir_combustible(distancia)
        else:
            print("No hay suficiente combustible para mover esa distancia.")


class SistemaCombustible:
    def __init__(self) -> None:
        self.combustible = 100

    def verificar_combustible(self, distancia: int) -> bool:
        return self.combustible >= distancia * 0.5

    def reducir_combustible(self, distancia: int):
        self.combustible -= distancia * 0.5

    def obtener_combustible(self) -> None:
        print(f"existe esta cantida de combustible: {self.combustible}")


# ---------------------- opcion 2
class Auto3:
    def __init__(self, tanque) -> None:
        self.position = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia * 0.5:
            self.position += distancia
            self.tanque.usar_combustible(distancia * 0.5)
        else:
            print("No hay suficiente combustible para mover esa distancia.")


class TanqueCombustible1:
    def __init__(self) -> None:
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad


# ---------------------- 3
class TanqueCombustible2:
    """Responsabilidad: Almacenar y gestionar nivel de combustible"""

    def __init__(self, capacidad: float = 100.0):
        self._combustible = capacidad

    def tiene_suficiente(self, cantidad: float) -> bool:
        return self._combustible >= cantidad

    def extraer(self, cantidad: float):
        if cantidad > self._combustible:
            raise ValueError("Combustible insuficiente")
        self._combustible -= cantidad

    def agregar(self, cantidad: float):
        self._combustible += cantidad

    @property
    def nivel(self) -> float:
        return self._combustible


class Motor:
    """Responsabilidad: Calcular consumo según eficiencia"""

    def __init__(self, eficiencia: float = 0.5):
        self.litros_por_km = eficiencia

    def calcular_consumo(self, distancia: float) -> float:
        return distancia * self.litros_por_km


class Auto4:
    """Responsabilidad: Coordinar movimiento"""

    def __init__(self, tanque: TanqueCombustible2, motor: Motor):
        self.posicion = 0
        self.tanque = tanque
        self.motor = motor

    def mover(self, distancia: float) -> bool:
        consumo_necesario = self.motor.calcular_consumo(distancia)

        if self.tanque.tiene_suficiente(consumo_necesario):
            self.tanque.extraer(consumo_necesario)
            self.posicion += distancia
            return True
        return False
