def esNumeroStep(numero):
    numero_str = str(numero)
    for i in range(len(numero_str) - 1):
        if abs(int(numero_str[i]) - int(numero_str[i + 1])) != 1:
            return False

    return True

numero_usuario = int(input("Ingresa un número \n >>> "))
resultado = esNumeroStep(numero_usuario)

if resultado:
    print(f"{numero_usuario} es un número step.")
else:
    print(f"{numero_usuario} no es un número step.")
