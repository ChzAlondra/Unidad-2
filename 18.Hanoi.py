"""
def hanoi(n, origen, destino, auxiliar):
    if n == 1:    # Caso base: solo un disco
        print(f"Mover disco de {origen} a {destino}")
    else:         # Caso recursivo
        hanoi(n-1, origen, auxiliar, destino)  # Mover n-1 discos al auxiliar
        hanoi(1, origen, destino, auxiliar)    # Mover disco mayor al destino
        hanoi(n-1, auxiliar, destino, origen)  # Mover n-1 discos al destino

hanoi(3, "A", "C", "B")
"""

class TorresHanoi:
    def __init__(self, n, origen="A", destino="C", auxiliar="B"):
        """
        Constructor que recibe:
        - n: número de discos
        - origen: nombre de la torre origen
        - destino: nombre de la torre destino
        - auxiliar: nombre de la torre auxiliar
        """
        self.n = n
        self.origen = origen
        self.destino = destino
        self.auxiliar = auxiliar

    def resolver(self):
        """
        Resuelve el problema de las Torres de Hanoi usando recursión.
        Imprime los movimientos de los discos.
        """
        self._hanoi_recursivo(self.n, self.origen, self.destino, self.auxiliar)

    def _hanoi_recursivo(self, n, origen, destino, auxiliar):
        """
        Método recursivo interno:
        - Caso base: n == 1 → mover disco directamente
        - Caso recursivo: mover n-1 discos al auxiliar, disco mayor al destino, n-1 discos al destino
        """
        if n == 1:
            print(f"Mover disco de {origen} a {destino}")
        else:
            self._hanoi_recursivo(n-1, origen, auxiliar, destino)
            self._hanoi_recursivo(1, origen, destino, auxiliar)
            self._hanoi_recursivo(n-1, auxiliar, destino, origen)


# Ejemplo de uso:
torres = TorresHanoi(3)
torres.resolver()
