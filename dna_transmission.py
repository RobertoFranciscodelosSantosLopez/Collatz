import math
import random

def medir_agoniza_adn(n_inicial):
    n = n_inicial
    conteo_debilitado = 0
    entro_en_reduccion = False
    
    while n > 1:
        bits_str = bin(n)[2:]
        rho = bits_str.count('1') / len(bits_str)
        
        # Detectamos el momento exacto en que entra en tu umbral de Reducción Pura
        if rho < 0.30 and not entro_en_reduccion:
            entro_en_reduccion = True
            
        if entro_en_reduccion:
            conteo_debilitado += 1

        if (n & (n - 1)) == 0:
            return conteo_debilitado, int(math.log2(n))

        n = (3 * n + 1) if n % 2 != 0 else n // 2
    return 0, 0

if __name__ == "__main__":
    print(f"\n--- TIEMPO DE VIDA EN REDUCCIÓN PURA ---")
    print(f"{'Nº':<3} | {'Pasos en Agonía':<18} | {'Salto Final (2^x)'}")
    print("-" * 50)
    for i in range(10):
        pasos, exp = medir_agoniza_adn(random.getrandbits(64) | 1)
        print(f"{i+1:<3} | {pasos:<18} | 2^{exp}")
