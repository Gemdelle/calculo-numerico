"""
Unidad 2: Raíces de ecuaciones no lineales — Ejercicio 4
========================================================

Consigna:
- Sea p_n una sucesión definida por p_n = sum_{k=1}^n (1/k).
  Demuestre que p_n − p_{n−1} = 1/n; sin embargo, p_n es la n-ésima suma parcial
  de la serie armónica divergente. Conclusiones.

Este script verifica la identidad y visualiza la divergencia de la serie.
"""

import numpy as np
import matplotlib.pyplot as plt


def harmonic_sum(n: int) -> float:
    if n < 1:
        raise ValueError("n debe ser un número positivo")
    return sum(1.0 / i for i in range(1, n + 1))


def demonstrate_difference(n: int):
    if n < 2:
        raise ValueError("n debe ser mayor que 1 para calcular la diferencia")
    pn = harmonic_sum(n)
    pn_1 = harmonic_sum(n - 1)
    difference = pn - pn_1
    expected = 1.0 / n
    return difference, expected


def plot_harmonic_series(n_max: int) -> None:
    n_values = np.arange(1, n_max + 1)
    partial_sums = [harmonic_sum(n) for n in n_values]

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, partial_sums, 'b-', label='Suma parcial pₙ')
    plt.grid(True, alpha=0.3)
    plt.xlabel('n')
    plt.ylabel('pₙ')
    plt.title('Sumas Parciales de la Serie Armónica')
    plt.legend()

    # Referencia log(n)
    log_reference = np.log(n_values)
    plt.plot(n_values, log_reference, 'r--', label='ln(n) (referencia)')
    plt.legend()
    plt.show()


def main() -> None:
    print("1. Demostración de (pₙ - pₙ₋₁) = 1/n:")
    for n in [2, 5, 10, 100]:
        diff, expected = demonstrate_difference(n)
        print(f"n = {n}:")
        print(f"   pₙ - pₙ₋₁ = {diff}")
        print(f"   1/n = {expected}")
        print(f"   Error absoluto = {abs(diff - expected)}\n")

    print("\n2. Demostración de la divergencia:")
    for n in [10, 100, 1000, 10000]:
        sum_n = harmonic_sum(n)
        print(f"Suma parcial para n = {n}: {sum_n}")

    print("\n3. Generando gráfica de las sumas parciales...")
    plot_harmonic_series(1000)

    print("\nConclusiones:")
    print("1. Se verifica que (pₙ - pₙ₋₁) = 1/n para todo n ≥ 1")
    print("2. La serie armónica es divergente, como evidencian las sumas parciales y su comparación con ln(n)")


if __name__ == "__main__":
    main()
