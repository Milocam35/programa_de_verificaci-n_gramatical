import os
import sys

def es_binario_capicua(cadena):
    for caracter in cadena:
        if caracter not in '01':
            print(f"El símbolo '{caracter}' no es válido.")
            return False

    longitud = len(cadena)
    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud - i - 1]:
            return False
    return True

def leer_binario_desde_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido.strip()
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_archivo}")
        return None

# Obtener la ruta del directorio actual
directorio_actual = os.path.dirname(sys.argv[0])

# Definir las rutas de los tres archivos
nombres_archivos = [
    "Gramatica1_Correcta.txt",
    "Gramatica1_Incorrecta.txt",
    "Gramatica1_IncorrectaCaracter.txt"
]

# Procesar cada archivo y aplicar la función es_binario_capicua a su contenido
for nombre_archivo in nombres_archivos:
    ruta_archivo = os.path.join(directorio_actual, nombre_archivo)
    cadena = leer_binario_desde_archivo(ruta_archivo)
    print(f"\nVerificando el archivo: {cadena}")

    if cadena is not None:
        if es_binario_capicua(cadena):
            print("La cadena es aceptada.")
        else:
            print("La cadena NO es aceptada.")
