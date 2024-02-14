import numpy as np

#Para gramática 4

class DFA:
    def __init__(self, estados, alfabeto, estado_inicial, estados_aceptacion, tabla_transiciones):
        self.estados = estados
        self.alfabeto = alfabeto
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.tabla_transiciones = tabla_transiciones

    def procesar_cadena(self, cadena):
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                print(f"Caracter {simbolo} no definido")
                return False
            simbolo_index = self.alfabeto.index(simbolo)
            estado_actual = self.tabla_transiciones[self.estados.index(estado_actual)][simbolo_index]
            if estado_actual is None:
                return False
        return estado_actual in self.estados_aceptacion

estados = ['q0', 'q1', 'q2']
alfabeto = ['a', 'b']
estado_inicial = 'q0'
estados_aceptacion = ['q0', 'q2']
tabla_transiciones = np.array([
    ['q1', None],
    [None, 'q2'],
    [None, 'q0'],
])

automata = DFA(estados, alfabeto, estado_inicial, estados_aceptacion, tabla_transiciones)

cadena = input("Ingrese una cadena: ")
if automata.procesar_cadena(cadena):
    print("La cadena es aceptada por el autómata.")
else:
    print("La cadena NO es aceptada por el autómata.")
