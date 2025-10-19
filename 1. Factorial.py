"""
def factorial(n):
    if n == 1:           # Caso base: cuando n llega a 1, se detiene la recursión
        return 1
    else:                # Caso recursivo: multiplica n por el factorial del número anterior
        return n * factorial(n-1)

print(factorial(5))      # Llama a la función y muestra 120
"""

class Factorial:
    def __init__(self, n):
        """
        Constructor que recibe un número entero positivo n.
        """
        self.n = n

    def calcular(self):
        """
        Calcula el factorial del número usando recursión.
        Retorna el resultado del factorial.
        """
        return self._factorial_recursivo(self.n)

    def _factorial_recursivo(self, n):
        """
        Método interno recursivo que calcula el factorial.
        Caso base: si n == 1 devuelve 1.
        Caso recursivo: n * factorial(n-1)
        """
        if n == 1:
            return 1
        else:
            return n * self._factorial_recursivo(n - 1)


# Ejemplo de uso:
numero = Factorial(5)
print(numero.calcular())  # 120