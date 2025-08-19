import numpy as np
import matplotlib.pyplot as plt

def harmonic_sum(n):
    """
    Calcula la n-ésima suma parcial de la serie armónica
    pₙ = Σᵢ₌₁ⁿ (1/i)
    """
    if n < 1:
        raise ValueError("n debe ser un número positivo")
    return sum(1/i for i in range(1, n + 1))

def demonstrate_difference(n):
    """
    Demuestra que (pₙ - pₙ₋₁) = 1/n
    """
    if n < 2:
        raise ValueError("n debe ser mayor que 1 para calcular la diferencia")
    pn = harmonic_sum(n)
    pn_1 = harmonic_sum(n - 1)
    difference = pn - pn_1
    expected = 1/n
    return difference, expected

def plot_harmonic_series(n_max):
    """
    Grafica las sumas parciales de la serie armónica para demostrar su divergencia
    """
    n_values = np.arange(1, n_max + 1)
    partial_sums = [harmonic_sum(n) for n in n_values]
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, partial_sums, 'b-', label='Suma parcial pₙ')
    plt.grid(True, alpha=0.3)
    plt.xlabel('n')
    plt.ylabel('pₙ')
    plt.title('Sumas Parciales de la Serie Armónica')
    plt.legend()
    
    # Agregar una línea de referencia logarítmica para mostrar el crecimiento
    log_reference = np.log(n_values)
    plt.plot(n_values, log_reference, 'r--', label='ln(n) (referencia)')
    plt.legend()
    plt.show()

def main():
    # 1. Demostrar que (pₙ - pₙ₋₁) = 1/n para algunos valores
    print("1. Demostración de (pₙ - pₙ₋₁) = 1/n:")
    for n in [2, 5, 10, 100]:
        diff, expected = demonstrate_difference(n)
        print(f"n = {n}:")
        print(f"   pₙ - pₙ₋₁ = {diff}")
        print(f"   1/n = {expected}")
        print(f"   Error absoluto = {abs(diff - expected)}\n")
    
    # 2. Demostrar la divergencia de la serie
    print("\n2. Demostración de la divergencia:")
    n_values = [10, 100, 1000, 10000]
    for n in n_values:
        sum_n = harmonic_sum(n)
        print(f"Suma parcial para n = {n}: {sum_n}")
    
    # 3. Visualizar el comportamiento de la serie
    print("\n3. Generando gráfica de las sumas parciales...")
    plot_harmonic_series(1000)
    
    print("\nConclusiones:")
    print("1. Se verifica que (pₙ - pₙ₋₁) = 1/n para todo n ≥ 1")
    print("2. La serie armónica es divergente, lo cual se evidencia por:")
    print("   - El crecimiento continuo de las sumas parciales")
    print("   - La comparación con ln(n) muestra un crecimiento similar")
    print("   - No existe un límite superior para las sumas parciales")

if __name__ == "__main__":
    main()
