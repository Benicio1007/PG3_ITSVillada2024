class triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lados = [lado1, lado2, lado3]

    def imprimir_lado_mayor(self):
        lado_mayor = max(self.lados)
        print("El lado mayor es:", lado_mayor)

    def es_equilatero(self):
        if len(set(self.lados)) == 1:
            print("Es equilatero")
        else:
            print("No es equilatero")

lado1 = float(input("Ingrese la longitud del primer lado \n >>> "))
lado2 = float(input("Ingrese la longitud del segundo lado \n >>> "))
lado3 = float(input("Ingrese la longitud del tercer lado \n >>> "))

triangulo = triangulo(lado1, lado2, lado3)
triangulo.imprimir_lado_mayor()
triangulo.es_equilatero()
