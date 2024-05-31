def index_of(lst, value): 
    try:
        return lst.index(value)
    except ValueError:
        return -1

lista = [8,12,9,45]

entrada_usuario = int(input("Ingrese un numero a buscar \n >>>"))

indice = index_of(lista,entrada_usuario)

if indice == -1:
    print("El numero no se encontro")
else:
    print(f"El numero {entrada_usuario} se encontro en el indice {indice}")