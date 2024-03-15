class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def establecer_nombre(self, nombre):
        self.nombre = nombre
    def mostrar_nombre(self):
        print("Nombre:", self.nombre)

persona1 = Persona("Benicio")
persona2 = Persona("Soledad")
persona1.mostrar_nombre()
persona2.mostrar_nombre()
