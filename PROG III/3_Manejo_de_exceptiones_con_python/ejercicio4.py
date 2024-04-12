def division_numeros():
    while True:
        try:
            
            num1 = float(input("Ingrese el primer número: \n >>>"))
            num2 = float(input("Ingrese el segundo número \n >>> "))
            
            resultado = num1 / num2
            
            print("La división de", num1, "entre", num2, "es:", resultado)
            
            
            break
        except ValueError:
            print("Error: Debe ingresar números.")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")

division_numeros()
