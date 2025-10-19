"""
def es_palindromo(palabra):
    if len(palabra) <= 1:            # Caso base: palabra vacía o de 1 letra siempre es palíndromo
        return True
    elif palabra[0] != palabra[-1]:  # Si la primera y última letra no son iguales, no es palíndromo
        return False
    else:                            # Caso recursivo: compara el interior de la palabra
        return es_palindromo(palabra[1:-1])

print(es_palindromo("anilina"))      # Imprime True
"""

class Palindromo:
    def __init__(self, palabra):
        """
        Constructor que recibe una palabra o cadena de texto.
        """
        self.palabra = palabra.lower()  # Convertimos a minúsculas para evitar errores de comparación

    def comprobar(self):
        """
        Verifica si la palabra es un palíndromo usando recursividad.
        Retorna True si lo es, False en caso contrario.
        """
        return self._es_palindromo_recursivo(self.palabra)

    def _es_palindromo_recursivo(self, palabra):
        """
        Método interno recursivo que compara el primer y último carácter.
        Caso base: si la longitud es 0 o 1 → True.
        Caso recursivo:
            - Si los extremos son iguales → llama con la subcadena interior.
            - Si son distintos → False.
        """
        if len(palabra) <= 1:
            return True
        elif palabra[0] != palabra[-1]:
            return False
        else:
            return self._es_palindromo_recursivo(palabra[1:-1])


# Ejemplo de uso:
texto = Palindromo("anilina")
print(texto.comprobar())  # True
