import matplotlib.pyplot as plt

def get_v2(n):
    count = 0
    if n == 0: return 0
    while n % 2 == 0:
        count += 1
        n //= 2
    return count

def collatz_steps(n):
    steps = 0
    curr = n
    while curr > 1:
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = 3 * curr + 1
        steps += 1
    return steps

def analizar_presion_vecindad(rango_inicio, muestras):
    resultados = []
    for i in range(rango_inicio, rango_inicio + muestras):
        if i % 2 == 0: continue
        
        v2_n = get_v2(3 * i + 1)
        if v2_n == 1: # Es un rebelde (Expansivo Débil)
            # Medimos la "Presión" de los vecinos cercanos (n-4, n-2, n+2, n+4)
            vecinos = [i-4, i-2, i+2, i+4]
            presion = sum([get_v2(3 * v + 1) for v in vecinos])
            
            pasos = collatz_steps(i)
            resultados.append({'n': i, 'presion': presion, 'pasos': pasos})
    return resultados

# Ejecutamos en el rango de 1 millón
print("Analizando fricción de bits en el rango 1,000,001...")
data = analizar_presion_vecindad(1000001, 10000)

# Ordenar por presión (de mayor a menor)
data_sorted = sorted(data, key=lambda x: x['presion'], reverse=True)

print(f"\n--- RESULTADOS DE FRICCIÓN (N={len(data)}) ---")
print(f"Top 5 con MÁXIMA PRESIÓN (Rodeados de fuertes):")
for d in data_sorted[:5]:
    print(f"n: {d['n']} | Presión: {d['presion']} | Pasos: {d['pasos']}")

print(f"\nTop 5 con MÍNIMA PRESIÓN (Aislados/Libres):")
for d in data_sorted[-5:]:
    print(f"n: {d['n']} | Presión: {d['presion']} | Pasos: {d['pasos']}")

# Cálculo de promedios para comparar
high_p = [d['pasos'] for d in data_sorted[:50]]
low_p = [d['pasos'] for d in data_sorted[-50:]]

print(f"\n--- COMPARATIVA DE PROMEDIOS (Muestra de 50) ---")
print(f"Promedio Pasos con Alta Presión: {sum(high_p)/50:.2f}")
print(f"Promedio Pasos con Baja Presión: {sum(low_p)/50:.2f}")
