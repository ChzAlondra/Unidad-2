"""
def contar_digitos(n):
    if n < 10:              # Caso base: si el número tiene un solo dígito
        return 1
    else:                   # Caso recursivo: cuenta 1 y continúa con el número sin el último dígito
        return 1 + contar_digitos(n // 10)

print(contar_digitos(12345))  # Imprime 5
"""

class ContadorDigitos:
    def __init__(self, n):
        """
        Constructor que recibe un número entero positivo n.
        """
        self.n = n

    def contar(self):
        """
        Devuelve la cantidad de dígitos del número usando recursión.
        """
        return self._contar_recursivo(self.n)

    def _contar_recursivo(self, n):
        """
        Método interno recursivo que cuenta los dígitos de n.
        Caso base: si n < 10, devuelve 1.
        Caso recursivo: 1 + contar los dígitos del número sin su último dígito.
        """
        if n < 10:
            return 1
        else:
            return 1 + self._contar_recursivo(n // 10)


# Ejemplo de uso:
numero = ContadorDigitos(12345)
print(numero.contar())  # 5
