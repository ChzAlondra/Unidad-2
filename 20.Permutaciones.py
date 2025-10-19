"""
def permutaciones(lista, inicio=0):
    if inicio == len(lista) - 1:  # Caso base: último índice → imprime lista
        print(lista)
    else:
        for i in range(inicio, len(lista)):
            lista[inicio], lista[i] = lista[i], lista[inicio]  # Intercambio
            permutaciones(lista, inicio + 1)                   # Llamada recursiva
            lista[inicio], lista[i] = lista[i], lista[inicio]  # Revertir intercambio

permutaciones([1, 2, 3])
"""

class GeneradorPermutaciones:
    def __init__(self, lista):
        """
        Constructor que recibe la lista de elementos a permutar.
        """
        self.lista = lista

    def generar(self):
        """
        Genera e imprime todas las permutaciones posibles de la lista usando recursión.
        """
        self._permutaciones_recursivo(self.lista, 0)

    def _permutaciones_recursivo(self, lista, inicio):
        """
        Método recursivo interno:
        - Caso base: inicio == len(lista)-1 → imprime la permutación actual
        - Caso recursivo: intercambia elementos y llama recursivamente
        - Revierte el intercambio para mantener la lista original
        """
        if inicio == len(lista) - 1:
            print(lista)
        else:
            for i in range(inicio, len(lista)):
                lista[inicio], lista[i] = lista[i], lista[inicio]  # Intercambio
                self._permutaciones_recursivo(lista, inicio + 1)   # Llamada recursiva
                lista[inicio], lista[i] = lista[i], lista[inicio]  # Revertir intercambio


# Ejemplo de uso:
perm = GeneradorPermutaciones([1, 2, 3])
perm.generar()
