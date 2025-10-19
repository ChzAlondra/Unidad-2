"""
def es_primo(n, divisor=2):
    if n <= 2:                  # Caso especial: 2 es primo, 1 o 0 no
        return n == 2
    if n % divisor == 0:        # Si divisible → no es primo
        return False
    if divisor * divisor > n:   # Si divisor supera raíz cuadrada → primo
        return True
    return es_primo(n, divisor+1)  # Llamada recursiva con siguiente divisor

print(es_primo(13))            # Imprime True
"""

class VerificadorPrimo:
    def __init__(self, numero):
        """
        Constructor que recibe el número a verificar si es primo.
        """
        self.numero = numero

    def es_primo(self):
        """
        Determina si el número es primo usando recursión.
        Retorna True si es primo, False si no lo es.
        """
        return self._es_primo_recursivo(self.numero, 2)

    def _es_primo_recursivo(self, n, divisor):
        """
        Método recursivo interno:
        - Caso especial: n <= 2 → True si n==2
        - Si divisible por divisor → False
        - Si divisor^2 > n → True
        - Llamada recursiva con divisor+1
        """
        if n <= 2:
            return n == 2
        if n % divisor == 0:
            return False
        if divisor * divisor > n:
            return True
        return self._es_primo_recursivo(n, divisor + 1)


# Ejemplo de uso:
numero = VerificadorPrimo(13)
print(numero.es_primo())  # True
