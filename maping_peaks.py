import random

def medir_resistencia_probabilistica(cantidad, bits):
    print(f"\n--- RESISTENCIA A LA PROBABILIDAD (Axioma López) ---")
    print(f"{'ID':<3} | {'Picos Superados':<15} | {'Valles de Fuga':<15} | {'Resultado'}")
    print("-" * 65)

    encontrados = 0
    while encontrados < cantidad:
        n = random.getrandbits(bits) | 1
        intentos_colapso = 0
        fugas = 0
        pasos = 0
        
        while n > 1 and pasos < 5000:
            rho = bin(n)[2:].count('1') / len(bin(n)[2:])
            
            # Un pico es un intento de la probabilidad por cerrar el ciclo
            if rho >= 0.85: 
                intentos_colapso += 1
            # Un valle es una fuga exitosa
            if rho <= 0.25:
                fugas += 1
            
            if (n & (n - 1)) == 0: break
            n = (3 * n + 1) if n % 2 != 0 else n // 2
            pasos += 1
        
        if pasos > 400: # Analizamos solo los que tienen historia
            encontrados += 1
            print(f"{encontrados:<3} | {intentos_colapso:<15} | {fugas:<15} | ATRAPADO EN {pasos}")

if __name__ == "__main__":
    medir_resistencia_probabilistica(10, 64)
