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

def verificar_patron_27(n):
    # El ADN del 27: v2 de [n-4, n-2, n+2, n+4]
    return [get_v2(3*(n + d) + 1) for d in [-4, -2, 2, 4]]

def test_herencia_escalar():
    patron_objetivo = [1, 2, 3, 1]
    print(f"{'Base^Exp':<15} | {'Valor n':<20} | {'Patrón v2':<15} | {'Pasos':<6} | {'¿Hereda?'}")
    print("-" * 75)
    
    bases_a_probar = [3, 19, 35] # Las que detectamos antes
    
    for base in bases_a_probar:
        for exp in range(1, 25, 2): # Exponentes impares
            n = base**exp
            patron = verificar_patron_27(n)
            hereda = "SÍ (CLON)" if patron == patron_objetivo else "-"
            pasos = collatz_steps(n)
            
            # Solo imprimimos resultados interesantes o cambios de patrón
            if hereda == "SÍ (CLON)" or exp < 5:
                print(f"{str(base)+'^'+str(exp):<15} | {str(n)[:18]+'..':<20} | {str(patron):<15} | {pasos:<6} | {hereda}")

test_herencia_escalar()
