class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre: str = nombre
        self.edad: int = edad

    def hablar(self):
        print("hola, yo puedo hablar")

    def get_edad(self):
        print(f'tengo: {self.edad}')


class Alumno(Persona):
    def __init__(self, nombre: str, edad: int, curso: str) -> None:
        super().__init__(nombre, edad)
        self.curso = curso


# alumno1 = Alumno("Jose", 14, "ingles")
# print(alumno1.curso)
# alumno1.hablar()


########## Herencia multiple
class Artista:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

    def habilidad(self):
        print(f"soy un artista de tipo: {self.tipo}")


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre: str, edad: int, tipo: str, sueldo: int) -> None:
        # super().__init__(nombre, edad)
        self.nombre = nombre # funciona esto porque los atributos pertenecen al objeto, no a la clase
        self.edad = edad
        self.tipo = tipo
        self.sueldo = sueldo

# no es recomendable usar esto porque la inicializacion es manual
# si crece la clase Artista en atributos se tendria que actualizar manualmente las clases hijas
# se rompe la responsabilidad de la clase
empleado1 = EmpleadoArtista("jose", 15, "plastico", 5000)
print(empleado1.tipo)
empleado1.habilidad() # esto funciona porque el objeto tiene el atributo tipo, y la funcion encuentra el atributo y funciona
empleado1.get_edad()
print(EmpleadoArtista.__mro__)

###### Manera correcta de multi-herencia
class Animal:
    def __init__(self, nombre: str, edad: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.nombre = nombre
        self.edad = edad


class Volador:
    def __init__(self, alas: bool, **kwargs):
        super().__init__(**kwargs)
        self.alas = alas
    
    def habilidad(self):
        if self.alas:
            print(f"puedo volar: {self.alas}")
        else:
            print("no puedo volar")


class Ave(Animal, Volador):
    def __init__(self, nombre: str, edad: int, alas: bool):
        super().__init__(nombre=nombre, edad=edad, alas=alas)
# (<class '__main__.Ave'>, <class '__main__.Animal'>, <class '__main__.Volador'>, <class 'object'>)
# super() siempre llama al siguiente en MRO, no necesariamente al padre
# paso 1:
# super().__init__(nombre=nombre, edad=edad, alas=alas)
# paso 2: 
# def __init__(self, nombre, edad, **kwargs):
#     super().__init__(**kwargs)
#     self.nombre = nombre
#     self.edad = edad
# # nombre="paloma"
# edad=3
# kwargs = {"alas": True}
# paso 3:
# def __init__(self, alas, **kwargs):
#     super().__init__(**kwargs)
#     self.alas = alas


print(Ave.__mro__)
ave = Ave("paloma", 3, True)
ave.habilidad()

######### MRO method resolution order
# class A:
#     def hablar(self):
#         print("hola desde A")


# class B:
#     def hablar(self):
#         print("hola desde B")


# class C:
#     def hablar(self):
#         print("hola desde C")


# class D:
#     def hablar(self):
#         pass
#         print("hola desde D")


# d = D()
# d.hablar()
