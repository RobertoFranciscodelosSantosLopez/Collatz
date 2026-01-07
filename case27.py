def get_v2(n):
    if n == 0: return 0
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    return count

def collatz_steps(n):
    steps = 0
    curr = n
    while curr > 1:
        if curr % 2 == 0: curr //= 2
        else: curr = (3 * curr + 1) // 2
        steps += 1
    return steps

# 1. Extraemos el patrón de vecindad del 27 (sus 4 vecinos impares más cercanos)
n_ref = 27
patron_27 = [get_v2(3*(n_ref + d) + 1) for d in [-4, -2, 2, 4]]
print(f"Patrón de fuerza (v2) alrededor del 27: {patron_27}")

def buscar_clones_del_27(rango_inicio, muestras):
    print(f"\nBuscando números con la misma vecindad que el 27 en el rango {rango_inicio}...")
    encontrados = 0
    for i in range(rango_inicio, rango_inicio + muestras):
        if i % 2 == 0: continue
        
        # Obtenemos el patrón del número actual
        patron_actual = [get_v2(3*(i + d) + 1) for d in [-4, -2, 2, 4]]
        
        if patron_actual == patron_27:
            encontrados += 1
            pasos = collatz_steps(i)
            print(f"¡Clon encontrado! n: {i} | Pasos: {pasos} (vs 111 del 27)")
    
    if encontrados == 0:
        print("No se encontraron clones exactos. La vecindad del 27 es muy específica.")

buscar_clones_del_27(1, 1000) # Buscamos en los primeros 1000
buscar_clones_del_27(1000001, 10000) # Buscamos en el rango del millón
