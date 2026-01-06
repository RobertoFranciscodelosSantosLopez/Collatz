import random
import sys
import time

# Permitimos que Python maneje el string de salida para un millón de bits
sys.set_int_max_str_digits(1000000)

def experimento_limite_infinito(bits):
    # Generar el monstruo de un millón de bits
    n = random.getrandbits(bits) | 1
    
    ke = 0  # Inyecciones (3n+1)
    kr = 0  # Extracciones (n//2)
    inicio = time.time()
    
    print(f"--- INICIANDO VALIDACIÓN DE 1,000,000 DE BITS ---")
    print(f"Magnitud: 10^{bits//3.32:.0f} aproximadamente.")
    
    while n > 1:
        if n % 2 != 0:
            n = 3 * n + 1
            ke += 1
        else:
            # Extracción masiva de bits (Valuación 2-ádica rápida)
            v2 = (n & -n).bit_length() - 1
            kr += v2
            n >>= v2
        
        # Reporte de progreso cada 100k pasos
        if (ke + kr) % 500000 == 0:
            print(f"Bits restantes: {n.bit_length()} | Ratio actual: {kr/ke:.6f}")

    fin = time.time()
    ratio = kr / ke
    return ke, kr, ratio, fin - inicio

# Ejecución
bits_objetivo = 1000000
ke, kr, ratio, duracion = experimento_limite_infinito(bits_objetivo)

print(f"\n--- RESULTADOS DEL LÍMITE INFINITO ---")
print(f"Tiempo de ejecución: {duracion:.2f} segundos")
print(f"Relación Intrínseca (E): {ratio:.8f}")
print(f"Veredicto: {'CONVERGENCIA ABSOLUTA' if 1.99 <= ratio <= 2.01 else 'DESVIACIÓN DINÁMICA'}")
