def dibujar_rectangulo(ancho, alto, caracter):
    for i in range(alto):
        print(caracter * ancho)

def dibujar_triangulo(base, caracter):
    for i in range(1, base + 1):
        print(caracter * i)


while True:
    opcion = input("¿Qué deseas dibujar? (R para rectángulo, T para triángulo) o deseas salir (S) \n >>> ")
    
    if opcion.upper() == 'R':
        ancho_rectangulo = int(input("Ingrese el ancho del rectángulo \n >>> "))
        alto_rectangulo = int(input("Ingrese el alto del rectángulo \n >>> "))
        caracter_rectangulo = input("Ingrese el carácter para el rectángulo \n >>> ")
        dibujar_rectangulo(ancho_rectangulo, alto_rectangulo, caracter_rectangulo)
    
    elif opcion.upper() == 'T':
        base_triangulo = int(input("Ingrese la base del triángulo \n >>> "))
        caracter_triangulo = input("Ingrese el carácter para el triángulo \n >>>")
        print("\nTriángulo:")
        dibujar_triangulo(base_triangulo, caracter_triangulo)
    else:
        print("Opción no válida. Por favor, selecciona R para rectángulo o T para triángulo.")
    
    if opcion.upper() == 'S':
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, selecciona R para rectángulo o T para triángulo. Tambien para salir(S)")
