"""
def combinaciones(cadena, actual=""):
    if cadena == "":           # Caso base: cadena vacía → imprime combinación actual
        print(actual)
    else:                      # Caso recursivo: incluir o no el primer carácter
        combinaciones(cadena[1:], actual + cadena[0])  # Incluir
        combinaciones(cadena[1:], actual)             # No incluir

combinaciones("ab")
"""

class CombinacionesCadena:
    def __init__(self, cadena):
        """
        Constructor que recibe la cadena de la cual generar combinaciones.
        """
        self.cadena = cadena

    def generar(self):
        """
        Genera todas las combinaciones posibles de los caracteres de la cadena usando recursión.
        Imprime cada combinación.
        """
        self._combinaciones_recursivo(self.cadena, "")

    def _combinaciones_recursivo(self, cadena, actual):
        """
        Método recursivo interno:
        - Caso base: cadena vacía → imprime la combinación actual
        - Caso recursivo: generar combinaciones incluyendo o no el primer carácter
        """
        if cadena == "":
            print(actual)
        else:
            self._combinaciones_recursivo(cadena[1:], actual + cadena[0])  # Incluir
            self._combinaciones_recursivo(cadena[1:], actual)             # No incluir


# Ejemplo de uso:
c = CombinacionesCadena("ab")
c.generar()
