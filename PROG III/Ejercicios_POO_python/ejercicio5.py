class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cargar_datos(self):
        self.nombre = input("Ingrese el nombre de la persona \n >>> ")
        self.edad = input("Ingrese la edad de la persona \n >>> ")

    def imprimir_datos(self):
        print("Nombre \n >>>", self.nombre)
        print("Edad \n >>>", self.edad)


if __name__ == "__main__":
    persona = persona("", 0)
    persona.cargar_datos()
    persona.imprimir_datos()
