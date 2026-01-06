import math

def analizar_base(b):
    if b % 2 == 0: return None
    temp = b
    stats = {"w": 0, "s": 0}
    while temp > 1:
        if temp % 2 != 0:
            temp = 3 * temp + 1
            v2 = (temp & -temp).bit_length() - 1
            if v2 == 1: stats["w"] += 1
            else: stats["s"] += 1
            temp >>= v2
    
    total = stats["w"] + stats["s"]
    return (stats["s"] / total) if total > 0 else 0

print(f"{'Base':<10} | {'Densidad (ρ)':<15} | {'Naturaleza':<20} | {'Predicción López'}")
print("-" * 70)

bases_rebeldes = []
for i in range(3, 201, 2): # Probamos las primeras 100 bases impares
    rho = analizar_base(i)
    if rho is None: continue
    
    # Clasificación según tu taxonomía
    if rho < 0.45:
        nat = "Expansivo Rebelde"
        pred = "Estabilización Lenta"
        bases_rebeldes.append((i, rho))
    elif rho >= 0.55:
        nat = "Colapsador Nato"
        pred = "Caída Fulminante"
    else:
        nat = "Equilibrado"
        pred = "Colapso Estándar"
        
    if i < 35 or rho < 0.45: # Mostramos los primeros y los rebeldes detectados
        print(f"{i:<10} | {rho:<15.4f} | {nat:<20} | {pred}")

# Cálculo de la Constante de López Proyectada para la base más difícil (27)
# Usando los datos previos: rho(27)=0.4146, rho(27^1000)=0.4931
rho_b = 0.4146
rho_bk = 0.4931
k = 1000
# Despejando una lambda simplificada: lambda = ( (diff_base / diff_potencia) - 1 ) / log(k)
lambda_L = (( (0.5 - rho_b) / (0.5 - rho_bk) ) - 1) / math.log10(k)

print(f"\n--- CONSTANTE DE ESTABILIZACIÓN DE LÓPEZ (λL) ---")
print(f"Valor calculado basado en 27^1000: {lambda_L:.6f}")
