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

def es_potencia(n):
    if n <= 1: return None
    # Probamos bases desde 2 hasta la raíz del número
    for base in range(2, int(n**0.5) + 1):
        p = 2
        while base**p <= n:
            if base**p == n:
                return (base, p)
            p += 1
    return None

def analizar_herencia_rebelde(rango_inicio, muestras):
    print(f"--- INVESTIGACIÓN DE HERENCIA: Rango {rango_inicio} a {rango_inicio + muestras} ---")
    patron_27 = [1, 2, 3, 1] # v2 de [n-4, n-2, n+2, n+4]
    
    hallazgos = 0
    for i in range(rango_inicio, rango_inicio + muestras):
        if i % 2 == 0: continue
        
        # Verificamos si cumple el "ADN de vecindad" del 27
        patron_actual = [get_v2(3*(i + d) + 1) for d in [-4, -2, 2, 4]]
        
        if patron_actual == patron_27:
            hallazgos += 1
            potencia = es_potencia(i)
            pasos = collatz_steps(i)
            
            if potencia:
                base, exp = potencia
                print(f"[*] ¡HERENCIA ENCONTRADA! n: {i} ({base}^{exp}) | Pasos: {pasos}")
            elif i < 500: # Mostrar originales pequeños para referencia
                print(f"[ ] Rebelde de base n: {i} | Pasos: {pasos}")

    if hallazgos == 0:
        print("No se encontraron clones en este rango.")

# Ejecución profunda
analizar_herencia_rebelde(1, 100000)
