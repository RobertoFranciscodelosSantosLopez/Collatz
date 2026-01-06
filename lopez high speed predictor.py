import math
import sys

# Configuración para manejar números masivos si fuera necesario
sys.set_int_max_str_digits(1000000)

def analizar_base(b):
    """Analiza la firma de paridad (ADN) de la base."""
    if b % 2 == 0: return None
    temp = b
    stats = {"w": 0, "s": 0}
    while temp > 1:
        if temp % 2 != 0:
            temp = 3 * temp + 1
            # Valuación 2-ádica (fuerza de división)
            v2 = (temp & -temp).bit_length() - 1
            if v2 == 1: stats["w"] += 1
            else: stats["s"] += 1
            temp >>= v2
    total = stats["w"] + stats["s"]
    return (stats["s"] / total) if total > 0 else 0

def prediccion_lopez_escala(base, bits_objetivo, lambda_L=3.7922):
    """Aplica el Teorema de Estabilización para predecir colapso en escalas masivas."""
    rho_base = analizar_base(base)
    
    if rho_base is None:
        return "Error: La base debe ser un número impar."

    # k representa el factor de escala de la potencia o magnitud de bits
    # Usamos una relación logarítmica para la dilución de la anomalía
    k_equivalente = bits_objetivo / 10 
    
    # Ecuación de la Fuerza Restauradora de López
    rho_proyectado = 0.5 - ((0.5 - rho_base) / (1 + lambda_L * math.log10(k_equivalente)))
    
    print(f"--- ORÁCULO DE LÓPEZ: PREDICCIÓN ASINTÓTICA ---")
    print(f"Base Analizada: {base}")
    print(f"Escala de Prueba: 10^{bits_objetivo} bits")
    print(f"Densidad Original (ADN): {rho_base:.4f}")
    print(f"Densidad Proyectada a escala: {rho_proyectado:.6f}")
    
    # Umbral crítico de Collatz (Log2(3) - 1 ≈ 0.585 -> requerimiento de rho > 0.366)
    UMBRAL_CRITICO = 0.366
    
    if rho_proyectado > UMBRAL_CRITICO:
        return f"VERDICTO: CONVERGENCIA ABSOLUTA (Supera umbral de {UMBRAL_CRITICO})"
    else:
        return "VERDICTO: EXPANSIÓN TEMPORAL (Requiere más bits para estabilizar)"

# --- EJECUCIÓN DE PRUEBA DE ALTO NIVEL ---
# Probamos al "Rebelde 151" en una escala de un BILLÓN de bits
print(prediccion_lopez_escala(151, 1000000000))
