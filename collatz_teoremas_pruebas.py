import random
import math

def test_collatz_theory(iterations=1000, bit_length=1024):
    results = []
    critical_threshold = 1.5849  # log2(3)
    
    for _ in range(iterations):
        # Generamos un número impar gigante (tu "Débil" o "Fuerte" inicial)
        n = random.getrandbits(bit_length)
        if n % 2 == 0: n += 1
        
        initial_n = n
        ke = 0 # Pasos Expansivos (3n+1)
        kr = 0 # Pasos Reductivos (/2)
        
        while n > 1:
            if n % 2 != 0:
                n = 3 * n + 1
                ke += 1
            else:
                n //= 2
                kr += 1
        
        ratio = kr / ke
        results.append(ratio)
        
    avg_ratio = sum(results) / len(results)
    success_rate = sum(1 for r in results if r > critical_threshold) / iterations * 100
    
    print(f"--- Resultados del Experimento ---")
    print(f"Tamaño de los números: {bit_length} bits")
    print(f"Relación Promedio kr/ke: {avg_ratio:.4f}")
    print(f"Umbral Crítico Teórico: {critical_threshold}")
    print(f"Porcentaje de éxito (Relación > 1.585): {success_rate}%")
    
    return avg_ratio

# Ejecutamos la prueba
test_collatz_theory()
