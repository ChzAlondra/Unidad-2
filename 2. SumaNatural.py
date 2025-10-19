"""
def suma_natural(n):
    if n == 1:              # Caso base: cuando n llega a 1, se detiene la recursión
        return 1
    else:                   # Caso recursivo: suma n con la suma de los números anteriores
        return n + suma_natural(n-1)

print(suma_natural(5))      # Imprime 15
"""

class SumaNatural:
    def __init__(self, n):
        """
        Constructor que recibe un número entero positivo n.
        """
        self.n = n

    def calcular(self):
        """
        Calcula la suma de todos los números desde 1 hasta n usando recursión.
        Retorna el resultado de la suma.
        """
        return self._suma_recursiva(self.n)

    def _suma_recursiva(self, n):
        """
        Método interno recursivo que realiza la suma.
        Caso base: si n == 1 devuelve 1.
        Caso recursivo: n + suma(n - 1)
        """
        if n == 1:
            return 1
        else:
            return n + self._suma_recursiva(n - 1)


# Ejemplo de uso:
numero = SumaNatural(5)
print(numero.calcular())  # 15
