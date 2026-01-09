import random
import time

def experimento_monstruo_8192():
    # 1. GENERACIÓN (Aseguramos que sea impar de 8192 bits)
    bits_iniciales = 8192
    n = random.getrandbits(bits_iniciales) | 1
    n_copia = n # Para el bucle
    
    # 2. INFERENCIA DE LÓPEZ (Tu Teorema)
    L = bits_iniciales / 14.26
    picos_estimados = 80 # Densidad observada
    prediccion_base = int(picos_estimados * L)
    techo_rebelde = int(prediccion_base * 1.5) # +50% de tu constante Cl
    
    print(f"--- SISTEMA DE INFERENCIA DE LÓPEZ ---")
    print(f"Predicción Base (Ciudadano): {prediccion_base} pasos")
    print(f"Techo de Mutante (Rey Rebelde): {techo_rebelde} pasos")
    print("-" * 40)
    print(f"Iniciando colapso del Monstruo de 8192 bits...")

    # 3. CÁLCULO REAL
    inicio = time.time()
    pasos = 0
    max_bits = n.bit_length()
    
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
            if n.bit_length() > max_bits:
                max_bits = n.bit_length()
        pasos += 1
    
    fin = time.time()
    tiempo_total = fin - inicio

    # 4. RESULTADOS FINALES
    print(f"\n--- RESULTADOS REALES ---")
    print(f"Pasos Totales: {pasos}")
    print(f"Expansión Máxima: {max_bits} bits")
    print(f"Tiempo de cómputo: {tiempo_total:.4f} segundos")
    
    # Verificación del Axioma II (Expansión Suicida)
    if pasos <= techo_rebelde:
        print("\nESTADO: VALIDADO. El número sucumbió dentro del margen de López.")
    else:
        print("\nESTADO: EXCEPCIÓN. Se ha encontrado un Mutante de grado superior.")

# Ejecutar todo
experimento_monstruo_8192()
