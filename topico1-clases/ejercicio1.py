class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


nombre = input("nombre: ")
edad = input("edad: ")

estudiante = Estudiante(nombre, edad)

print(f"""
      Datos del estudiante: \n\n
        Nombre: {estudiante.nombre} \n
        Edad: {estudiante.edad}
""")
