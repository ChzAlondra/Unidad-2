# Reglas de Prioridad: Min-Heap (el número más bajo tiene la prioridad más alta)
# 1. Cliente VIP/Senior (Max 3 saltos)
# 2. Cliente Estándar (Max 2 saltos)
# 3. Cliente Nuevo/No-Cliente (0 saltos)

class ColaConPrioridadLimitada:
    def __init__(self):
        self.items = []
        
    def queue(self, prioridad, nombre):
        elemento = (prioridad, nombre)
        
        if prioridad == 1:
            limite_salto = 3
        elif prioridad == 2:
            limite_salto = 2
        else:
            limite_salto = 0
        
        posicion = len(self.items)
        
        saltos = 0
        for i in range(len(self.items) - 1, -1, -1):
            prioridad_actual = self.items[i][0]
            
            if prioridad < prioridad_actual and saltos < limite_salto:
                posicion = i
                saltos += 1
            else:
                break
        
        self.items.insert(posicion, elemento)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return ' '.join([f"{p[1]}(P:{p[0]})" for p in self.items])

FilaBanco = [
    (2, "Ana"),
    (3, "Bruno"),
    (2, "Carlos"),
    (1, "Diana"),
    (3, "Elena"),
    (2, "Felipe"),
    (2, "Gabriela"),
    (3, "Hugo"),
    (1, "Irene"),
    (1, "Javier")
]

ColaBanco = ColaConPrioridadLimitada()

print("--- Proceso de Encolado con Saltos Limitados ---")
for prioridad, nombre in FilaBanco:
    ColaBanco.queue(prioridad, nombre)
    print(f"Llega {nombre} (P:{prioridad}). Cola: {ColaBanco}")

print("\n--- Orden de Atención en Ventanilla ---")
while not ColaBanco.is_empty():
    p, nombre = ColaBanco.dequeue()
    print(f"Atendiendo -> {nombre} (Prioridad: {p})")
