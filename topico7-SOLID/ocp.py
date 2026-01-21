# OCP: una clase debe estar abierta para su extension,
# pero cerrado para su modificacion
from abc import ABC, abstractmethod


class CalculadoraDescuentos:
    def calcular_descuentos(self, tipo: str, monto: float) -> float:
        if tipo == "regular":
            return monto * 0.95
        elif tipo == "vip":
            return monto * 0.80
        elif tipo == "empleado":
            return monto * 0.90
        else:
            raise ValueError("tipo no valido")


cal = CalculadoraDescuentos()
print(cal.calcular_descuentos("regular", 20))


# ###################### SOLUCION ######################
class EstrategiaDescuento(ABC):
    @abstractmethod
    def calcular_descuentos(self, monto: float) -> float:
        pass


class DescuentoRegular(EstrategiaDescuento):
    def calcular_descuentos(self, monto: float) -> float:
        return monto * 0.95


class DescuentoVip(EstrategiaDescuento):
    def calcular_descuentos(self, monto: float) -> float:
        return monto * 0.80


class DescuentoEmpleado(EstrategiaDescuento):
    def calcular_descuentos(self, monto: float) -> float:
        return monto * 0.90


class CalculadoraDescuentos2:
    def __init__(self, estrategia: EstrategiaDescuento) -> None:
        self.estrategia = estrategia

    def calcular(self, monto: float) -> float:
        return self.estrategia.calcular_descuentos(monto)


cal2 = CalculadoraDescuentos2(DescuentoRegular())
print(cal2.calcular(20))

cal3 = CalculadoraDescuentos2(DescuentoVip())
print(cal3.calcular(20))
