"""
def decimal_a_binario(n):
    if n == 0:                        # Caso base: 0 → cadena vacía
        return ''
    else:                             # Caso recursivo: invoca con n//2 y concatena el resto
        return decimal_a_binario(n // 2) + str(n % 2)

print(decimal_a_binario(10))          # Imprime "1010"
"""

class DecimalABinario:
    def __init__(self, numero):
        """
        Constructor que recibe un número entero positivo.
        """
        self.numero = numero

    def convertir(self):
        """
        Convierte el número decimal a su representación binaria usando recursión.
        Retorna una cadena con el binario.
        """
        if self.numero == 0:
            return "0"  # Caso especial para 0
        return self._decimal_a_binario_recursivo(self.numero)

    def _decimal_a_binario_recursivo(self, n):
        """
        Método recursivo interno:
        - Caso base: n == 0 → devuelve cadena vacía
        - Caso recursivo: invoca con n//2 y concatena el resto
        """
        if n == 0:
            return ''
        else:
            return self._decimal_a_binario_recursivo(n // 2) + str(n % 2)


# Ejemplo de uso:
numero = DecimalABinario(10)
print(numero.convertir())  # "1010"
