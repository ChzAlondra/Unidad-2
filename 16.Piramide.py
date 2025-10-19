"""
def piramide(n):
    if n == 0:           # Caso base: nivel 0 → no imprime nada
        return
    piramide(n-1)        # Llamada recursiva para niveles anteriores
    print('*' * n)       # Imprime la línea actual con n asteriscos

piramide(5)
"""

class Piramide:
    def __init__(self, niveles):
        """
        Constructor que recibe el número de niveles de la pirámide.
        """
        self.niveles = niveles

    def imprimir(self):
        """
        Imprime una pirámide de asteriscos de manera recursiva.
        """
        self._piramide_recursiva(self.niveles)

    def _piramide_recursiva(self, n):
        """
        Método recursivo interno:
        - Caso base: n == 0 → termina la recursión
        - Caso recursivo: llama al nivel anterior, luego imprime línea de n asteriscos
        """
        if n == 0:
            return
        self._piramide_recursiva(n - 1)
        print('*' * n)


# Ejemplo de uso:
p = Piramide(5)
p.imprimir()
