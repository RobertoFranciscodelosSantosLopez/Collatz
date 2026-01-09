import random

def analizar_resistencia_picos(bits):
    n_ini = random.getrandbits(bits) | 1
    n = n_ini
    
    stats = {"PI": 0, "PA": 0, "PS": 0}
    pasos = 0
    
    print(f"\n--- MAPEO DE RESISTENCIA POR TIPO DE PICO ---")
    
    while n > 1 and pasos < 5000:
        bits_str = bin(n)[2:]
        rho = bits_str.count('1') / len(bits_str)
        
        # Clasificación de la presión actual
        if rho >= 0.85: stats["PS"] += 1
        elif 0.66 <= rho <= 0.68: stats["PA"] += 1
        elif 0.58 <= rho < 0.66: stats["PI"] += 1
            
        if (n & (n - 1)) == 0: break
        n = (3 * n + 1) if n % 2 != 0 else n // 2
        pasos += 1

    print(f"ADN Inicial: {bin(n_ini)[:20]}...")
    print(f"Pasos Totales: {pasos}")
    print(f"Resistencia a Picos Inestables (Fugas potenciales): {stats['PI']}")
    print(f"Encuentros con el Punto Crítico (0.66): {stats['PA']}")
    print(f"Presiones de Saturación (Punto de quiebre): {stats['PS']}")
    print("-" * 55)

if __name__ == "__main__":
    for _ in range(5):
        analizar_resistencia_picos(64)
