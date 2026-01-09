import random

def clasificador_probabilidad_lopez(muestras, bits):
    l_teorica = bits / 14.26
    
    conteo = {"Sumiso": 0, "Ciudadano": 0, "Rey Rebelde": 0}
    
    print(f"--- ANALIZANDO TASA DE MUTACIÓN ({bits} BITS) ---")
    print(f"Buscando el 10% de probabilidad en {muestras} muestras...\n")

    for _ in range(muestras):
        n = random.getrandbits(bits) | 1
        temp_n = n
        pasos = 0
        picos_pi = 0
        
        while temp_n > 1:
            bits_str = bin(temp_n)[2:]
            rho = bits_str.count('1') / len(bits_str)
            if 0.58 <= rho <= 0.65: picos_pi += 1
            if (temp_n & (temp_n - 1)) == 0: break
            temp_n = (3 * temp_n + 1) if temp_n % 2 != 0 else temp_n // 2
            pasos += 1
        
        if picos_pi > 0:
            prediccion = picos_pi * l_teorica
            # Calculamos la desviación respecto a la Ley de López
            desviacion = ((pasos - prediccion) / pasos) * 100
            
            # Clasificación de Escenarios
            if desviacion > 30:
                conteo["Rey Rebelde"] += 1
            elif desviacion < -15:
                conteo["Sumiso"] += 1
            else:
                conteo["Ciudadano"] += 1

    # SALIDA DE RESULTADOS
    print(f"{'ESCENARIO':<15} | {'FRECUENCIA':<10} | {'PROBABILIDAD'}")
    print("-" * 45)
    for escenario, cantidad in conteo.items():
        prob = (cantidad / muestras) * 100
        print(f"{escenario:<15} | {cantidad:<10} | {prob:.2f}%")
    
    print("\n--- CONCLUSIÓN PRELIMINAR ---")
    if 8 <= (conteo["Rey Rebelde"]/muestras*100) <= 12:
        print("Tu intuición es EXACTA: Existe un 10% de Mutantes Rebeldes.")
    else:
        print(f"La tasa de mutación en esta escala es del {(conteo['Rey Rebelde']/muestras*100):.2f}%.")

if __name__ == "__main__":
    clasificador_probabilidad_lopez(500, 512)
