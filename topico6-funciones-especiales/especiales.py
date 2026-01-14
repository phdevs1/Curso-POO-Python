# class Persona:
#     def __init__(self, nombre: str, edad: int) -> None:
#         self.nombre = nombre
#         self.edad = edad
    
#     def __str__(self) -> str:
#         return f"Persona(nombre={self.nombre}, edad={self.edad})"
    

# persona1 = Persona("Juan", 30)
# print(persona1)  # Output: Persona(nombre=Juan, edad=30)


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Persona(nombre={self.nombre!r}, edad={self.edad!r})"

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"

    # sobrecarga del operador +
    def __add__(self, other):
        nuevo_valor = self.edad + other.edad
        return Persona(f"{self.nombre} & {other.nombre}", nuevo_valor)


per = Persona("Ana", 25)
print(str(per))   # Output: Ana tiene 25 años
print(repr(per))  # Output: Persona(nombre='Ana', edad=25)

per2 = Persona("Luis", 30)
per3 = per + per2
print(per3)   # Output: Ana & Luis tiene 55 años