def limpiar_y_ordenar(lista_enteros):
    return sorted(set(x for x in lista_enteros if x >= 0))

numeros = [4, -1, 2, 4, 3, -5, 2]
print(limpiar_y_ordenar(numeros))