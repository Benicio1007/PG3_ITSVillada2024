class operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.realizar_operaciones()

    def realizar_operaciones(self):
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        resultado = self.num1 + self.num2
        print(f"Suma: {self.num1} + {self.num2} = {resultado}")

    def resta(self):
        resultado = self.num1 - self.num2
        print(f"Resta: {self.num1} - {self.num2} = {resultado}")

    def multiplicacion(self):
        resultado = self.num1 * self.num2
        print(f"Multiplicación: {self.num1} * {self.num2} = {resultado}")

    def division(self):
        if self.num2 != 0:
            resultado = self.num1 / self.num2
            print(f"División: {self.num1} / {self.num2} = {resultado}")
        else:
            print("No se puede dividir")


num1 = int(input("Ingrese el primer número entero \n >>>"))
num2 = int(input("Ingrese el segundo número entero \n >>> "))

operaciones = operaciones(num1, num2)
