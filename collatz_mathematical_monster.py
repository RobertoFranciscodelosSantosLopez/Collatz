import random
import sys

# Aumentamos el límite de conversión de bits a string para manejar números gigantes
sys.set_int_max_str_digits(100000)

def gran_prueba_collatz(bits):
    # Generamos la semilla más grande de tu investigación
    n = random.getrandbits(bits) | 1
    semilla_original = n
    
    ke = 0  # Inyecciones (3n+1)
    kr = 0  # Extracciones (n//2)
    pasos = 0
    
    print(f"--- EXPERIMENTO DE ALTA ENTROPÍA ---")
    print(f"Semilla: {bits} bits (aprox. {len(str(n))} dígitos)")
    
    while n > 1:
        if n % 2 != 0:
            n = 3 * n + 1
            ke += 1
        else:
            # Optimizamos la extracción de bits
            v2 = (n & -n).bit_length() - 1
            kr += v2
            n >>= v2
        pasos += 1
        
        # Monitor de progreso cada 10k pasos
        if pasos % 10000 == 0:
            print(f"Procesando... Bits actuales: {n.bit_length()}")

    ratio = kr / ke if ke > 0 else 0
    return ke, kr, ratio, pasos

# Ejecutamos con 100,000 bits
bits_test = 100000
ke, kr, ratio, pasos = gran_prueba_collatz(bits_test)

print(f"\n--- RESULTADOS DEL 'SALTO DETERMINISTA' ---")
print(f"Total de operaciones: {pasos}")
print(f"Relación Intrínseca (E): {ratio:.6f}")
print(f"Diferencia con el límite 1.585: {ratio - 1.585:.6f}")
print(f"Veredicto: {'COLAPSO SEGURO' if ratio > 1.585 else 'ESTADO INDEFINIDO'}")
