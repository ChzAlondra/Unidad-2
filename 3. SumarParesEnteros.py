import time
import tracemalloc

def sumarPares(n):
    if type(n) != int or n < 3:
        raise Exception("n debe ser entero mayor que 2.")
    n -= n % 2
    return sumarParesAux(n)

def sumarParesAux(n):
    if n == 0:
        return 0
    else:
        return sumarParesAux(n - 2) + n
    
# --- Aquí medimos tiempo y memoria ---
tracemalloc.start()                       # Iniciar seguimiento de memoria
inicio = time.perf_counter_ns()           # Tiempo inicial

resultado = sumarPares(23)                # Guardamos el resultado

fin = time.perf_counter_ns()              # Tiempo final
mem_actual, mem_max = tracemalloc.get_traced_memory()

# Mostrar resultados
print(f"Suma de pares hasta N: {resultado}")
print(f"Tiempo de ejecución: {fin - inicio} nanosegundos")
print(f"Memoria actual usada: {mem_actual / 1024:.2f} KB")
print(f"Memoria máxima usada: {mem_max / 1024:.2f} KB")

tracemalloc.stop()
