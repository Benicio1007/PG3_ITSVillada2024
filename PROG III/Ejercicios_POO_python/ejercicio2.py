class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_informacion(self):
        print("Nombre \n>>>", self.nombre)
        print("Nota \n>>>", self.nota)

    def esta_regular(self):
        if self.nota >= 6:
            print("El alumno", self.nombre, "está regular.")
        else:
            print("El alumno", self.nombre, "no está regular.")

alumno1 = Alumno("Benicio", 7)
alumno2 = Alumno("Pedro", 5)

print("Información del primer alumno \n>>>")
alumno1.imprimir_informacion()
alumno1.esta_regular()

print("\nInformación del segundo alumno \n>>>")
alumno2.imprimir_informacion()
alumno2.esta_regular()