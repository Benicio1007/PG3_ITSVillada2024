def sumar_numeros():
    while True:
        try:
            num1 = int(input("Ingrese el primer número entero \n >>> "))
            num2 = int(input("Ingrese el segundo número entero \n >>> "))
            
            suma = num1 + num2
            
            print("La suma de", num1, "y", num2, "es \n >>>", suma)
            
            continuar = input("¿Quiere seguir sumando valores? (s/n) \n >>> ")
            
           
            if continuar.lower() != 's':
                break
        except ValueError:
            print("Error: Tiene ingresar números enteros. ")

sumar_numeros()
