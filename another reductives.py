import random

def mapear_puertos_de_entrada(cantidad, bits):
    print(f"\n--- MAPEO DE PUERTOS DE ENTRADA AL REDUCTIVO ---")
    print(f"{'Potencia 2':<15} | {'Frecuencia':<12} | {'ρ Promedio Pre-Choque'}")
    print("-" * 55)

    resultados = {}

    for _ in range(cantidad):
        n = random.getrandbits(bits) | 1
        while n > 1:
            next_n = (3 * n + 1) if n % 2 != 0 else n // 2
            if (next_n & (next_n - 1)) == 0 and next_n > 0:
                rho = bin(n)[2:].count('1') / len(bin(n)[2:])
                resultados[next_n] = resultados.get(next_n, []) + [rho]
                break
            n = next_n

    for p in sorted(resultados.keys()):
        avg_rho = sum(resultados[p]) / len(resultados[p])
        print(f"{p:<15} | {len(resultados[p]):<12} | {avg_rho:.4f}")

if __name__ == "__main__":
    # Analizamos 100 gigantes para ver la estadística real
    mapear_puertos_de_entrada(100, 64)
