"""
def buscar_elemento(lista, elemento):
    if not lista:               # Caso base: lista vacía → elemento no encontrado
        return False
    elif lista[0] == elemento:  # Caso éxito: primer elemento coincide
        return True
    else:                        # Caso recursivo: buscar en el resto de la lista
        return buscar_elemento(lista[1:], elemento)

print(buscar_elemento([1, 3, 5, 7], 5))  # Imprime True
"""

class BusquedaLista:
    def __init__(self, lista):
        """
        Constructor que recibe la lista de elementos.
        """
        self.lista = lista

    def contiene(self, elemento):
        """
        Verifica si el elemento está presente en la lista usando recursión.
        Retorna True si se encuentra, False en caso contrario.
        """
        return self._buscar_recursivo(self.lista, elemento)

    def _buscar_recursivo(self, lista, elemento):
        """
        Método recursivo interno:
        - Caso base: lista vacía → False
        - Caso éxito: primer elemento = elemento → True
        - Caso recursivo: buscar en el resto de la lista
        """
        if not lista:
            return False
        elif lista[0] == elemento:
            return True
        else:
            return self._buscar_recursivo(lista[1:], elemento)


# Ejemplo de uso:
busqueda = BusquedaLista([1, 3, 5, 7])
print(busqueda.contiene(5))  # True
