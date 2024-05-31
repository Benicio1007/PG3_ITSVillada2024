class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cargar_datos(self):
        self.nombre = input("Ingrese el nombre de la persona: \n >>>")
        self.edad = int(input("Ingrese la edad de la persona \n >>>"))

    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def debe_pagar_impuestos(self):
        if self.sueldo > 3000:
            print("El empleado debe pagar impuestos")
        else:
            print("El empleado no debe pagar impuestos")



if __name__ == "__main__":
    
    persona = Persona("", 0)

    persona.cargar_datos()

    persona.imprimir_datos()

    print("\n")

    nombre_empleado = input("Ingrese el nombre del empleado \n >>> ")
    edad_empleado = int(input("Ingrese la edad del empleado \n >>> "))
    sueldo_empleado = float(input("Ingrese el sueldo del empleado \n >>> "))

    empleado = Empleado(nombre_empleado, edad_empleado, sueldo_empleado)
  
    empleado.debe_pagar_impuestos()
