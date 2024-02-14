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

cadena = input("Ingrese una cadena binaria: ")
if es_binario_capicua(cadena):
    print("La cadena es aceptada.")
else:
    print("La cadena NO es aceptada.")