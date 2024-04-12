def obtener_nombre_mes():
    
    nombres_meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio",
                     "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    
    while True:
        try:
            
            numero_mes = int(input("Ingrese el número de mes (1-12) \n >>> "))
            
           
            nombre_mes = nombres_meses[numero_mes - 1]
            
           
            print("El mes correspondiente al número", numero_mes, "es:", nombre_mes)
            
           
            break
        except ValueError:
            print("Error: Debe ingresar un número entero. ")
        except IndexError:
            print("Error: El número de mes debe estar en el rango de 1 a 12. ")

obtener_nombre_mes()
