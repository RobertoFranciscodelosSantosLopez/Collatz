import random

def buscar_colapso_debil(intentos, bits):
    print(f"\n--- BUSCANDO EL ADN DÉBIL QUE COLAPSA (Límite Axiomático) ---")
    print(f"{'ID':<3} | {'ρ Final':<10} | {'Destino':<12} | {'Rareza'}")
    print("-" * 50)

    encontrados = 0
    min_rho = 1.0
    
    for i in range(intentos):
        n = random.getrandbits(bits) | 1
        while n > 1:
            next_n = (3 * n + 1) if n % 2 != 0 else n // 2
            
            if (next_n & (next_n - 1)) == 0 and next_n > 0:
                rho = bin(n)[2:].count('1') / len(bin(n)[2:])
                
                # Buscamos anomalías: Colapso con poca densidad (Débiles)
                if rho < 0.45:
                    encontrados += 1
                    rareza = "ALTA" if rho < 0.35 else "MEDIA"
                    print(f"{encontrados:<3} | {rho:<10.4f} | {next_n:<12} | {rareza}")
                    if rho < min_rho: min_rho = rho
                break
            n = next_n
            
    print("-" * 50)
    print(f"Récord de ADN más débil al morir: {min_rho:.4f}")

if __name__ == "__main__":
    # Forzamos una búsqueda intensiva
    buscar_colapso_debil(50000, 64)
