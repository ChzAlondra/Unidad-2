"""
def contar_caracter(cadena, caracter):
    if cadena == "":                  # Caso base: cadena vacía → 0
        return 0
    else:
        if cadena[0] == caracter:     # Coincidencia → suma 1
            return 1 + contar_caracter(cadena[1:], caracter)
        else:                         # No coincide → solo continua
            return contar_caracter(cadena[1:], caracter)

print(contar_caracter("banana", "a"))  # Imprime 3
"""

class ContadorCaracter:
    def __init__(self, cadena):
        """
        Constructor que recibe la cadena en la que se buscará el carácter.
        """
        self.cadena = cadena

    def contar(self, caracter):
        """
        Cuenta cuántas veces aparece el carácter en la cadena usando recursión.
        Retorna un entero con la cantidad de apariciones.
        """
        return self._contar_recursivo(self.cadena, caracter)

    def _contar_recursivo(self, cadena, caracter):
        """
        Método recursivo interno:
        - Caso base: cadena vacía → 0
        - Caso recursivo:
            - Si el primer carácter coincide → 1 + resto
            - Si no → solo contar en el resto
        """
        if cadena == "":
            return 0
        elif cadena[0] == caracter:
            return 1 + self._contar_recursivo(cadena[1:], caracter)
        else:
            return self._contar_recursivo(cadena[1:], caracter)


# Ejemplo de uso:
texto = ContadorCaracter("banana")
print(texto.contar("a"))  # 3
