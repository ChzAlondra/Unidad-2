import time
import tracemalloc

def imprimirParesHastaN(n):
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo")
    n -= n % 2
    imprimirParesHastaNAux(n)
    print()

def imprimirParesHastaNAux(n):
    if n == 0:
        return
    else:
        imprimirParesHastaNAux(n - 2)
        print(n, end=" ")

# --- Aquí medimos tiempo y memoria ---
tracemalloc.start()       # Iniciar seguimiento de memoria
inicio = time.perf_counter_ns()      # Tiempo inicial

imprimirParesHastaN(9)

fin = time.perf_counter_ns()         # Tiempo final
mem_actual, mem_max = tracemalloc.get_traced_memory()

print(f"\nTiempo de ejecución: {fin - inicio} nanosegundos")
print(f"Memoria actual usada: {mem_actual / 1024:.2f} KB")
print(f"Memoria máxima usada: {mem_max / 1024:.2f} KB")

tracemalloc.stop()
