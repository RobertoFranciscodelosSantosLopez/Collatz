import random
import sys

sys.set_int_max_str_digits(1000000)

def clasificar_dinamica_bits(bits):
    n = random.getrandbits(bits) | 1
    
    stats = {
        "omega_w": 0,  # Débiles (v2 = 1)
        "omega_s": 0,  # Fuertes (v2 >= 2)
        "max_v2": 0    # El "golpe" más fuerte detectado
    }
    
    print(f"--- CLASIFICANDO ESTADOS: {bits} BITS ---")
    
    while n > 1:
        if n % 2 != 0:
            n = 3 * n + 1
            # Analizamos la fuerza del par resultante
            v2 = (n & -n).bit_length() - 1
            
            if v2 == 1:
                stats["omega_w"] += 1
            else:
                stats["omega_s"] += 1
                if v2 > stats["max_v2"]:
                    stats["max_v2"] = v2
            
            n >>= v2
            
    return stats

# Ejecución para validar la distribución
bits_test = 1000000
resultados = clasificar_dinamica_bits(bits_test)

total_eventos = resultados["omega_w"] + resultados["omega_s"]
porcentaje_s = (resultados["omega_s"] / total_eventos) * 100

print(f"\n--- RESULTADOS DE TAXONOMÍA ---")
print(f"Eventos Expansivos Débiles (Omega_w): {resultados['omega_w']}")
print(f"Eventos Expansivos Fuertes (Omega_s): {resultados['omega_s']}")
print(f"Densidad de Colapso (Omega_s / Total): {porcentaje_s:.2f}%")
print(f"Máxima Valuación Detectada: v2 = {resultados['max_v2']}")
