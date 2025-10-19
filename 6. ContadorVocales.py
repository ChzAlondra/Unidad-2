"""
def contar_vocales(cadena):
    if cadena == "":                             # Caso base: si la cadena está vacía, no hay vocales
        return 0
    else:
        if cadena[0].lower() in 'aeiou':         # Si el primer carácter es vocal
            return 1 + contar_vocales(cadena[1:]) # Suma 1 y llama con el resto
        else:
            return contar_vocales(cadena[1:])     # Si no es vocal, continúa con el resto

print(contar_vocales("Recursividad"))  # Imprime 5
"""

class ContadorVocales:
    def __init__(self, cadena):
        """
        Constructor que recibe una cadena de texto.
        """
        self.cadena = cadena

    def contar(self):
        """
        Devuelve el número de vocales en la cadena usando recursión.
        """
        return self._contar_recursivo(self.cadena)

    def _contar_recursivo(self, cadena):
        """
        Método interno recursivo que cuenta las vocales.
        Caso base: si la cadena está vacía, devuelve 0.
        Caso recursivo:
            - Si el primer carácter es vocal, suma 1 y continúa.
            - Si no lo es, solo continúa con el resto de la cadena.
        """
        if cadena == "":
            return 0
        elif cadena[0].lower() in 'aeiou':
            return 1 + self._contar_recursivo(cadena[1:])
        else:
            return self._contar_recursivo(cadena[1:])


# Ejemplo de uso:
texto = ContadorVocales("Recursividad")
print(texto.contar())  # 5
