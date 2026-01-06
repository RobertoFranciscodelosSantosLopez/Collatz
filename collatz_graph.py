import matplotlib.pyplot as plt

def generate_transition_map(n):
    bits = []
    states = [] # 0 para Weak (3n+1)/2, 1 para Strong (v2 >= 2)
    trajectory = [n]
    
    temp_n = n
    while temp_n > 1:
        bits.append(temp_n.bit_length())
        
        if temp_n % 2 != 0:
            next_n = 3 * temp_n + 1
            v2 = 0
            while next_n % 2 == 0:
                next_n //= 2
                v2 += 1
            
            # Clasificación según tus axiomas
            if v2 == 1:
                states.append('Weak (Expansion)')
            else:
                states.append('Strong (Collapse)')
                
            temp_n = next_n
        else:
            temp_n //= 2
            # Las divisiones puras se consideran parte del efecto del último estado
            
        trajectory.append(temp_n)
        if len(bits) > 500: break # Límite para que la gráfica sea legible

    # Crear la gráfica
    plt.figure(figsize=(12, 6))
    plt.plot(bits, color='gray', alpha=0.5, label='Bit-length Path')
    
    # Resaltar las transiciones
    for i, state in enumerate(states):
        color = 'red' if 'Weak' in state else 'green'
        plt.scatter(i, bits[i], color=color, s=20, label=state if i < 2 else "")

    plt.title(f"State Transition Map for n (Log-Scale Entropy)")
    plt.xlabel("Iteration Step (k_e)")
    plt.ylabel("Entropy (Bit-length)")
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend(["Trajectory", "Weak State (Growth)", "Strong State (Reduction)"])
    plt.show()

# Ejemplo con un número "rebelde" de alta inercia
seed = (2**60) - 1 
generate_transition_map(seed)
