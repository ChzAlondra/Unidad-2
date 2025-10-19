"""
def mcd(a, b):
    if b == 0:                   # Caso base: si b llega a 0, el MCD es a
        return a
    else:                        # Caso recursivo: aplica el algoritmo de Euclides
        return mcd(b, a % b)

print(mcd(48, 18))               # Imprime 6
"""

class MCD:
    def __init__(self, a, b):
        """
        Constructor que recibe dos números enteros positivos.
        """
        self.a = a
        self.b = b

    def calcular(self):
        """
        Calcula el Máximo Común Divisor (MCD) de los dos números usando recursión.
        """
        return self._mcd_recursivo(self.a, self.b)

    def _mcd_recursivo(self, a, b):
        """
        Método interno recursivo que aplica el algoritmo de Euclides.
        Caso base: si b == 0, devuelve a.
        Caso recursivo: MCD(b, a % b)
        """
        if b == 0:
            return a
        else:
            return self._mcd_recursivo(b, a % b)


# Ejemplo de uso:
resultado = MCD(48, 18)
print(resultado.calcular())  # 6
