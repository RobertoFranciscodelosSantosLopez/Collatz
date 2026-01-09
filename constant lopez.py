import math

def collatz_steps_completos(n):
    steps = 0
    curr = n
    while curr > 1:
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = 3 * curr + 1
        steps += 1
    return steps

def test_final_lopez_preciso():
    print(f"{'Potencia':<10} | {'Pasos (S)':<10} | {'Constante L':<15} | {'Estado'}")
    print("-" * 70)
    
    for e in range(3, 40, 4):
        n = 3**e
        pasos = collatz_steps_completos(n)
        # Recalculamos L con la métrica de pasos reales
        L = pasos / math.log2(n)
        
        if e == 3:
            # Aquí confirmaremos los 111 pasos del 27
            estado = "NODO MAESTRO (111)"
        elif L > 15:
            estado = "REBELDE"
        else:
            estado = "SUICIDA"
            
        print(f"3^{e:<7} | {pasos:<10} | {L:<15.4f} | {estado}")

test_final_lopez_preciso()
