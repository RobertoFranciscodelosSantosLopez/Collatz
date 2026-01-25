import random

def get_collatz_metrics(n):
    steps = 0
    start_n = n
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n + 1) // 2 # Paso optimizado
            steps += 1 # Contamos expansiones fuertes
        steps += 1
    return steps

def hunt_villains(count=500, bit_length=68):
    villains = []
    print(f"Cazando {count} villanos de {bit_length} bits...")
    
    found = 0
    attempts = 0
    while found < count:
        # Generamos un número con alta densidad de 1s (potencial Mutante)
        candidate = random.getrandbits(bit_length) | 1 | (1 << (bit_length - 1))
        
        steps = get_collatz_metrics(candidate)
        
        # Filtramos solo los que presentan alta resistencia (Inercia > umbral)
        if steps > 500: 
            villains.append((candidate, steps))
            found += 1
            if found % 50 == 0:
                print(f"Progreso: {found}/{count} villanos capturados.")
        attempts += 1
    
    return villains

# Ejecución
results = hunt_villains(500, 68)

# Mostrar los 5 más "peligrosos"
results.sort(key=lambda x: x[1], reverse=True)
print("\n--- Top 5 Villanos de 68 bits (Mayor Inercia) ---")
for v, s in results[:5]:
    print(f"Valor: {v} | Pasos hasta 4,2,1: {s}")