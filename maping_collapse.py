import random

def analizar_punto_colision(cantidad, bits):
    print(f"\n--- ESTADO DEL ADN EN EL MOMENTO DEL CHOQUE ---")
    print(f"{'ID':<3} | {'ρ Antes del Choque':<20} | {'¿Era Fuerte?'} | {'Destino'}")
    print("-" * 65)

    for i in range(cantidad):
        n = random.getrandbits(bits) | 1
        rho_final = 0
        
        while n > 1:
            bits_str = bin(n)[2:]
            rho_final = bits_str.count('1') / len(bits_str)
            
            # Si el siguiente paso es un reductivo, este es el punto de choque
            next_n = (3 * n + 1) if n % 2 != 0 else n // 2
            if (next_n & (next_n - 1)) == 0 and next_n > 0:
                # Capturamos la densidad justo antes del "salto"
                estado = "SÍ (CHOQUE)" if rho_final > 0.50 else "NO (REDUCCIÓN)"
                print(f"{i+1:<3} | {rho_final:<20.4f} | {estado:<12} | {bin(next_n)}")
                break
            n = next_n

if __name__ == "__main__":
    analizar_punto_colision(10, 64)
