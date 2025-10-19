# Alondra Chavez Mendoza
# Estructura de datos Gpo C
# Ing.Sistemas computacionales
# 05/09/2025
# 1. Inicio
# 2. Declarar las variables globales: 
#    Pila <- vacía
#    Productos[3] <- {"Torta", "Sandwich", "Dobladita"}
#    Bebidas[3] <- {"Cafe", "Coca cola", "Juego"}
#    N <- 0
#    i <- 0
#    prod <- 0
#    prod_selc <- ""
#    beb <- 0
#    beb_selc <- ""
# 3. Escribir: "¿Cuántas personas llegaron a la cafetería?"
# 4. Leer: N
# 5. Para i <- 1 Hasta N Hacer
#    5.1 prod <- Random(0,2)  
#    5.2 prod_selc <- Productos[prod]
#    5.3 Apilar(Pila, prod)   
#    5.4 beb <- Random(0,2)   
#    5.5 beb_selc <- Bebidas[beb]
#    5.6 Apilar(Pila, beb)   
#    5.7 Escribir: "Persona ", i, " recibió: ", prod_selc, " y ", beb_selc
# 6. Fin Para
# 7. Fin

import random
import time
import tracemalloc

# Clase que representa la cafetería
class Cafeteria:
    def __init__(self):
        self.productos = ["Torta", "Sandwich", "Dobladita"]
        self.bebidas = ["Cafe", "Coca cola", "Juego"]
        self.pila = []

    def generar_pedido(self):
        # Selección aleatoria de producto
        prod = random.randint(0, 2)
        prod_selc = self.productos[prod]
        self.pila.append(prod_selc)

        # Selección aleatoria de bebida
        beb = random.randint(0, 2)
        beb_selc = self.bebidas[beb]
        self.pila.append(beb_selc)

        return prod_selc, beb_selc

# Programa principal
def main():
    cafeteria = Cafeteria()

    print("¿Cuántas personas llegaron a la cafetería?")
    N = int(input("Ingrese la cantidad: "))

    # Medición de tiempo y memoria
    tracemalloc.start()
    inicio = time.perf_counter()   # en segundos

    for i in range(1, N + 1):
        prod, beb = cafeteria.generar_pedido()
        print(f"Persona {i} recibió: {prod} y {beb}")

    fin = time.perf_counter()
    mem_actual, mem_max = tracemalloc.get_traced_memory()

    # Resultados
    print("\n--- Resultados de ejecución ---")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    print(f"Memoria actual usada: {mem_actual / 1024:.2f} KB")
    print(f"Memoria máxima usada: {mem_max / 1024:.2f} KB")

    tracemalloc.stop()

# Ejecutar el programa
main()


