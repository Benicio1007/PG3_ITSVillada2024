def esPalindromo(palabra):
    palabra = palabra.lower() 
    palabra_reversa = palabra[::-1] 

    return palabra == palabra_reversa  

palabra_usuario = input("Ingresa una palabra \n >>> ")
resultado = esPalindromo(palabra_usuario)
print(f"¿{palabra_usuario} es un palíndromo? {resultado}")
