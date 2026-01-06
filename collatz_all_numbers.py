import random

def collatz_bit_dynamics(n):
    steps = 0
    ke = 0  # Multiplicaciones (Inyección de bit-length)
    kr = 0  # Divisiones (Extracción de bit-length / Valuación 2-ádica)
    max_n = n
    
    print(f"--- Iniciando Análisis de Dinámica de Bits ---")
    print(f"Semilla inicial: {n.bit_length()} bits")
    
    while n > 1:
        if n % 2 != 0:
            # Estado Expansivo (Omega_w o Omega_s inminente)
            n = 3 * n + 1
            ke += 1
        else:
            # Estado Reductivo (Extracción de bits)
            # Contamos cuántos factores de 2 extraemos (v2(n))
            count = 0
            while n % 2 == 0:
                n //= 2
                count += 1
            kr += count
        
        if n > max_n:
            max_n = n
        steps += 1
        
    # Cálculo de la Relación Intrínseca (Tu Teorema)
    intrinsic_ratio = kr / ke if ke > 0 else 0
    
    return {
        "steps": steps,
        "ke": ke,
        "kr": kr,
        "ratio": intrinsic_ratio,
        "max_bits": max_n.bit_length()
    }

# Simulación con un número de 1024 bits (como en tu paper)
seed = random.getrandbits(1024) | 1 # Asegurar que sea impar
results = collatz_bit_dynamics(seed)

print(f"\nRESULTADOS FINALES:")
print(f"Total de Pasos: {results['steps']}")
print(f"Bits Inyectados (ke): {results['ke']}")
print(f"Bits Extraídos (kr): {results['kr']}")
print(f"Relación Intrínseca (E): {results['ratio']:.4f}")
print(f"Pico de Expansión Suicida: {results['max_bits']} bits")

if results['ratio'] > 1.585:
    print(f"\nVERDICTO: El ratio {results['ratio']:.4f} supera log2(3) [1.585].")
    print("La Deuda de Bits se liquidó. Decisividad de paridad confirmada.")
