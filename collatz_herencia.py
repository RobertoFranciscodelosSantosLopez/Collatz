import sys
sys.set_int_max_str_digits(1000000)

def analizar_personalidad(n, nombre):
    stats = {"w": 0, "s": 0}
    temp = n
    while temp > 1:
        if temp % 2 != 0:
            temp = 3 * temp + 1
            v2 = (temp & -temp).bit_length() - 1
            if v2 == 1: stats["w"] += 1
            else: stats["s"] += 1
            temp >>= v2
    
    total = stats["w"] + stats["s"]
    densidad = (stats["s"] / total) * 100
    print(f"Resultados para {nombre}:")
    print(f"  Eventos totales: {total}")
    print(f"  Densidad de Colapso (Omega_s): {densidad:.4f}%")
    return densidad

# Comparando la base con su potencia gigante
d1 = analizar_personalidad(27, "Base 27")
d2 = analizar_personalidad(27**1000, "Potencia 27^1000")

error = abs(d1 - d2)
print(f"\nDiferencia de 'Personalidad': {error:.4f}%")
