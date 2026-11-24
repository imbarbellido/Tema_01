def analizar_conjuntos(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    resultado = {
        "interseccion": conjunto1 & conjunto2,
        "union": conjunto1 | conjunto2,
        "diferencia_simetrica": conjunto1 ^ conjunto2
    }
    
    return resultado

l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
print(analizar_conjuntos(l1, l2))