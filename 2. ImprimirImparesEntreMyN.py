import time
import tracemalloc

def imprimirImparesEntreMyN(m, n):
    if type(m) != int:
        raise Exception("m debe ser entero positivo.")
    if type(n) != int or n <= m:
        raise Exception("n debe ser entero mayor que m.")
    m = m + 1 if m % 2 == 0 else m
    n = n - 1 if n % 2 == 0 else n
    imprimirImparesEntreMyNAux(m, n)

def imprimirImparesEntreMyNAux(m, n):
    if m > n:
        print()
    else:
        print(m, end = " ")
        imprimirImparesEntreMyNAux(m + 2, n)

# --- Aquí medimos tiempo y memoria ---
tracemalloc.start()       # Iniciar seguimiento de memoria
inicio = time.perf_counter_ns()      # Tiempo inicial

imprimirImparesEntreMyN(3,13)

fin = time.perf_counter_ns()         # Tiempo final
mem_actual, mem_max = tracemalloc.get_traced_memory()

print(f"\nTiempo de ejecución: {fin - inicio} nanosegundos")
print(f"Memoria actual usada: {mem_actual / 1024:.2f} KB")
print(f"Memoria máxima usada: {mem_max / 1024:.2f} KB")

tracemalloc.stop()