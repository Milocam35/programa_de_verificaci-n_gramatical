import numpy as np

#Para gramática 2

class DFA:
    def __init__(self, estados, alfabeto, estado_inicial, estados_aceptacion, tabla_transiciones):
        self.estados = estados
        self.alfabeto = alfabeto
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.tabla_transiciones = tabla_transiciones

    def procesar_cadena(self, cadena):
        a=0
        b=0
        estado_actual = self.estado_inicial
        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                print(f"Caracter {simbolo} no definido")
                return False 
            if (simbolo == 'a'):
              a+=1
            else: b+=1
            simbolo_index = self.alfabeto.index(simbolo)
            estado_actual = self.tabla_transiciones[self.estados.index(estado_actual)][simbolo_index]
            if estado_actual is None:
                return False

        if(b-a!=1):
          return False

        return estado_actual in self.estados_aceptacion

estados = ['q0', 'q1']
alfabeto = ['a', 'b']
estado_inicial = 'q0'
estados_aceptacion = ['q1']
tabla_transiciones = np.array([
    ['q0', 'q1'],
    [None, 'q1'],
])

automata = DFA(estados, alfabeto, estado_inicial, estados_aceptacion, tabla_transiciones)

cadena = input("Ingrese una cadena: ")
if automata.procesar_cadena(cadena):
    print("La cadena es aceptada por el autómata.")
else:
    print("La cadena NO es aceptada por el autómata.")