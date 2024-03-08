def ordenar_de_mayor_a_menor(lista):
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada

mi_lista = [5, 2, 8, 7, 12]
lista_ordenada = ordenar_de_mayor_a_menor(mi_lista)
print("Lista original:", mi_lista)
print("Lista ordenada:", lista_ordenada)