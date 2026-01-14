from abc import ABC, abstractmethod


# un metodo puede comportarse de distantas formas segun el objeto que lo use
class Animal:
    def hablar(self):
        print("El animal hace un sonido")


class Perro(Animal):
    def hablar(self):
        print("El perro dice: guau")


class Gato(Animal):
    def hablar(self):
        print("El gato dice: miau")


perro = Perro()
gato = Gato()
perro.hablar()  # Salida: El perro dice: guau
gato.hablar()   # Salida: El gato dice: miau


# metodos abstractos: obligar a las subclases a implementar ciertos metodos
class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto: float):
        pass


class Tarjeta(MetodoPago):
    def pagar(self, monto: float):
        print(f"Pagando {monto} con tarjeta")


class Paypal(MetodoPago):
    def pagar(self, monto: float):
        print(f"Pagando {monto} con PayPal")


# esto es interfaz, porque procesar_pago no sabe si es Tarjeta o Paypal
def procesar_pago(metodo: MetodoPago, monto: float):
    metodo.pagar(monto)


procesar_pago(Tarjeta(), 100)
procesar_pago(Paypal(), 200)


# Versión SIN polimorfismo

def procesar_pago2(tipo: str, monto: float):
    if tipo == "tarjeta":
        print(f"Pagando {monto} con tarjeta")
    elif tipo == "paypal":
        print(f"Pagando {monto} con PayPal")
    elif tipo == "transferencia":
        print(f"Pagando {monto} con transferencia")
    else:
        print("Método de pago no soportado")


procesar_pago2("tarjeta", 100)
procesar_pago2("paypal", 250)
procesar_pago2("transferencia", 500)
procesar_pago2("bitcoin", 300)   # No soportado
