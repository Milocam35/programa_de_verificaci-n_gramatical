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

# Definir las rutas de los tres archivos
rutas_archivos = [
    "programa_de_verificación_gramatical\Gramatica1_Correcta.txt",
    "programa_de_verificación_gramatical\Gramatica1_Incorrecta.txt",
    "programa_de_verificación_gramatical\Gramatica1_IncorrectaCaracter.txt"
]

# Procesar cada archivo y aplicar la función es_binario_capicua a su contenido
for ruta_archivo in rutas_archivos:
    cadena = leer_binario_desde_archivo(ruta_archivo)
    print(f"\nVerificando el archivo: {cadena}")

    if cadena is not None:
        if es_binario_capicua(cadena):
            print("La cadena es aceptada.")
        else:
            print("La cadena NO es aceptada.")

