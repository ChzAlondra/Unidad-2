"""
def suma_lista(lista):
    if not lista:                  # Caso base: si la lista está vacía, su suma es 0
        return 0
    else:                          # Caso recursivo: suma el primer elemento y llama con el resto
        return lista[0] + suma_lista(lista[1:])

print(suma_lista([1, 2, 3, 4, 5]))  # Imprime 15
"""

class SumaLista:
    def __init__(self, lista):
        """
        Constructor que recibe una lista de números.
        """
        self.lista = lista

    def calcular(self):
        """
        Devuelve la suma de todos los elementos de la lista usando recursión.
        """
        return self._suma_recursiva(self.lista)

    def _suma_recursiva(self, lista):
        """
        Método interno recursivo que realiza la suma.
        Caso base: si la lista está vacía, devuelve 0.
        Caso recursivo: suma el primer elemento y continúa con el resto.
        """
        if not lista:
            return 0
        else:
            return lista[0] + self._suma_recursiva(lista[1:])


# Ejemplo de uso:
numeros = SumaLista([1, 2, 3, 4, 5])
print(numeros.calcular())  # 15
