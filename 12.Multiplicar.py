"""
def multiplicar(a, b):
    if b == 0:           # Caso base: multiplicar por 0 → 0
        return 0
    else:                # Caso recursivo: suma a con la multiplicación de a y b-1
        return a + multiplicar(a, b-1)

print(multiplicar(3, 4))  # Imprime 12
"""

class Multiplicacion:
    def __init__(self, a, b):
        """
        Constructor que recibe dos números enteros a multiplicar.
        """
        self.a = a
        self.b = b

    def calcular(self):
        """
        Calcula la multiplicación de a y b usando sumas sucesivas recursivas.
        """
        return self._multiplicar_recursivo(self.a, self.b)

    def _multiplicar_recursivo(self, a, b):
        """
        Método recursivo interno:
        - Caso base: b == 0 → devuelve 0
        - Caso recursivo: suma a con la multiplicación de a y b-1
        """
        if b == 0:
            return 0
        else:
            return a + self._multiplicar_recursivo(a, b - 1)


# Ejemplo de uso:
resultado = Multiplicacion(3, 4)
print(resultado.calcular())  # 12
