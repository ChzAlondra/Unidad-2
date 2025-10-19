"""
def suma_digitos(n):
    if n == 0:                 # Caso base: n = 0 → devuelve 0
        return 0
    else:                      # Caso recursivo: último dígito + suma del resto
        return n % 10 + suma_digitos(n // 10)

print(suma_digitos(1234))     # Imprime 10
"""

class SumaDigitos:
    def __init__(self, numero):
        """
        Constructor que recibe un número entero positivo.
        """
        self.numero = numero

    def calcular(self):
        """
        Suma recursivamente los dígitos del número.
        """
        return self._suma_recursiva(self.numero)

    def _suma_recursiva(self, n):
        """
        Método recursivo interno:
        - Caso base: n == 0 → devuelve 0
        - Caso recursivo: último dígito + suma del resto
        """
        if n == 0:
            return 0
        else:
            return n % 10 + self._suma_recursiva(n // 10)


# Ejemplo de uso:
numero = SumaDigitos(1234)
print(numero.calcular())  # 10
