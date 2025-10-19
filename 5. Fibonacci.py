"""
def fibonacci(n):
    if n == 0 or n == 1:     # Casos base: F(0) = 0 y F(1) = 1
        return n
    else:                    # Caso recursivo: F(n) = F(n-1) + F(n-2)
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))          # Imprime 8
"""

class Fibonacci:
    def __init__(self, n):
        """
        Constructor que recibe la posición n del número de Fibonacci a calcular.
        """
        self.n = n

    def calcular(self):
        """
        Calcula el n-ésimo número de Fibonacci usando recursión.
        Retorna el resultado.
        """
        return self._fibonacci_recursivo(self.n)

    def _fibonacci_recursivo(self, n):
        """
        Método interno recursivo que calcula el número de Fibonacci.
        Casos base:
            F(0) = 0
            F(1) = 1
        Caso recursivo:
            F(n) = F(n-1) + F(n-2)
        """
        if n == 0 or n == 1:
            return n
        else:
            return self._fibonacci_recursivo(n - 1) + self._fibonacci_recursivo(n - 2)


# Ejemplo de uso:
numero = Fibonacci(6)
print(numero.calcular())  # 8
