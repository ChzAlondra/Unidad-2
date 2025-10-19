"""
def invertir_cadena(cadena):
    if len(cadena) == 0:           # Caso base: cadena vacía se devuelve igual
        return cadena
    else:                          # Caso recursivo: toma el último carácter + invierte el resto
        return cadena[-1] + invertir_cadena(cadena[:-1])

print(invertir_cadena("hola"))     # Imprime "aloh"
"""

class InversorCadena:
    def __init__(self, cadena):
        """
        Constructor que recibe la cadena que se desea invertir.
        """
        self.cadena = cadena

    def invertir(self):
        """
        Invierte la cadena utilizando recursividad.
        Retorna la cadena invertida.
        """
        return self._invertir_recursivo(self.cadena)

    def _invertir_recursivo(self, cadena):
        """
        Método recursivo interno:
        - Caso base: cadena vacía → retorna igual.
        - Caso recursivo: último carácter + inversión del resto.
        """
        if len(cadena) == 0:
            return cadena
        else:
            return cadena[-1] + self._invertir_recursivo(cadena[:-1])


# Ejemplo de uso:
texto = InversorCadena("hola")
print(texto.invertir())  # "aloh"
