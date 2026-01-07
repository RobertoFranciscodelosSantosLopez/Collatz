import statistics

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
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = (3 * curr + 1) // 2 # Usamos el paso abreviado para mayor precisión
        steps += 1
    return steps

def analizar_distancia_y_densidad(rango_inicio, muestras):
    resultados = []
    
    for i in range(rango_inicio, rango_inicio + muestras):
        if i % 2 == 0: continue
        
        # Solo estudiamos a los "rebeldes" (Expansivos Débiles)
        if get_v2(3 * i + 1) == 1:
            pasos = collatz_steps(i)
            
            # Buscamos la distancia al reductivo fuerte más cercano (v2 >= 3)
            distancia = 0
            encontrado = False
            for d in range(2, 100, 2): # Buscamos en un radio de 100 números
                if get_v2(3 * (i + d) + 1) >= 3 or get_v2(3 * (i - d) + 1) >= 3:
                    distancia = d
                    encontrado = True
                    break
            
            if encontrado:
                resultados.append({
                    'n': i,
                    'dist': distancia,
                    'pasos': pasos
                })
    return resultados

# Ejecución
print("Calculando radio de influencia y supervivencia...")
data = analizar_distancia_y_densidad(1000001, 20000)

# Agrupamos pasos por distancia
distancias_unicas = sorted(list(set([d['dist'] for d in data])))
print(f"\n{'Distancia al Fuerte':<20} | {'Promedio de Pasos':<20} | {'N':<5}")
print("-" * 50)

for dist in distancias_unicas:
    grupo = [d['pasos'] for d in data if d['dist'] == dist]
    if len(grupo) > 5: # Solo promedios significativos
        avg_pasos = sum(grupo) / len(grupo)
        print(f"{dist:<20} | {avg_pasos:<20.2f} | {len(grupo):<5}")
