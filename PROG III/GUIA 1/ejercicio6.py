def contarVocales(frase):
    frase = frase.lower()
    vocales = "aeiou"
    cantidad_vocales = sum(1 for letra in frase if letra in vocales)
    return cantidad_vocales

frase_usuario = input("Ingresa una frase \n >>> ")
resultado = contarVocales(frase_usuario)

print(f"La frase '{frase_usuario}' tiene {resultado} vocales.")
