import time
import tracemalloc

def contarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return contarDigitosAux(n)

def contarDigitosAux(n):
    if n < 10:
        return 1
    else:
        return contarDigitosAux(n // 10) + 1
    
# --- Aquí medimos tiempo y memoria ---
tracemalloc.start()                       # Iniciar seguimiento de memoria
inicio = time.perf_counter_ns()           # Tiempo inicial

resultado = contarDigitos(2574)           # Guardamos el resultado

fin = time.perf_counter_ns()              # Tiempo final
mem_actual, mem_max = tracemalloc.get_traced_memory()

# Mostrar resultados
print(f"Cantidad de dígitos: {resultado}")
print(f"Tiempo de ejecución: {fin - inicio} nanosegundos")
print(f"Memoria actual usada: {mem_actual / 1024:.2f} KB")
print(f"Memoria máxima usada: {mem_max / 1024:.2f} KB")

tracemalloc.stop()
