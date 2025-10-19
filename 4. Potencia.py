
"""
def potencia(a, b):
    if b == 0:             # Caso base: cualquier número elevado a 0 es 1
        return 1
    else:                  # Caso recursivo: multiplica a por a^(b-1)
        return a * potencia(a, b-1)

print(potencia(2, 3))      # Imprime 8
"""

class Potencia:
    def __init__(self, base, exponente):
        """
        Constructor que recibe la base y el exponente (enteros).
        """
        self.base = base
        self.exponente = exponente

    def calcular(self):
        """
        Calcula la potencia base^exponente usando recursión.
        Retorna el resultado de la operación.
        """
        return self._potencia_recursiva(self.base, self.exponente)

    def _potencia_recursiva(self, a, b):
        """
        Método interno recursivo que calcula la potencia.
        Caso base: si b == 0, devuelve 1.
        Caso recursivo: a * a^(b-1)
        """
        if b == 0:
            return 1
        else:
            return a * self._potencia_recursiva(a, b - 1)


# Ejemplo de uso:
resultado = Potencia(2, 3)
print(resultado.calcular())  # 8
