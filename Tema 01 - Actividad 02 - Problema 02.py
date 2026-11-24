import string

def contar_frecuencia_palabras(lista_palabras, ruta_fichero):
    signos = string.punctuation + "¿¡"
    tabla_limpieza = str.maketrans("", "", signos)
    
    palabras_objetivo = [p.lower().translate(tabla_limpieza) for p in lista_palabras]
    frecuencias = {palabra: 0 for palabra in sorted(set(palabras_objetivo))}
    
    with open(ruta_fichero, "r", encoding="utf-8") as fichero:
        texto = fichero.read().lower()
        texto_limpio = texto.translate(tabla_limpieza)
        palabras_texto = texto_limpio.split()
        
        for palabra in palabras_texto:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
                
    return frecuencias

nombre_archivo = "ejemplo.txt"
with open(nombre_archivo, "w", encoding="utf-8") as f:
    f.write("¡Hola mundo! Python es genial. El mundo de Python es muy amplio, ¿verdad?")

palabras_a_buscar = ["Python", "mundo", "java", "es"]
resultado = contar_frecuencia_palabras(palabras_a_buscar, nombre_archivo)

for palabra, conteo in sorted(resultado.items()):
    print(f"{palabra}: {conteo}")