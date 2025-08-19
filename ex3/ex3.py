"""
Unidad 2: Raíces de ecuaciones no lineales — Ejercicio 3
========================================================

Consigna:
- Aplique el algoritmo de la bisección a la ecuación (4x − 7)/(x − 2)^2 = 0
  usando los intervalos [1.5, 2.2] y [1.5, 2.5]. Explique gráficamente los resultados.
  Respuestas:
  a) Converge a 1.75
  b) Da como resultado p1 = 2 y f(2) no está definida

Este script aplica bisección en ambos intervalos, reporta resultados y grafica la función
con su asíntota vertical en x = 2.
"""

import time
import numpy as np
import matplotlib.pyplot as plt

try:
	from common_functions import bisection_method, print_bisection_table
except ImportError:
	import os as _os
	import sys as _sys
	_sys.path.append(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
	from common_functions import bisection_method, print_bisection_table


def f(x: float) -> float:
    if x == 2:
        raise ValueError("f(x) no está definida en x=2")
    return (4 * x - 7) / ((x - 2) ** 2)


def plot_function(roots=None, intervals=None):
    x_left = np.linspace(-14, 1.9, 1000)
    x_right = np.linspace(2.1, 20, 1000)

    y_left = []
    y_right = []
    for xi in x_left:
        try:
            y_left.append(f(xi))
        except ValueError:
            y_left.append(np.nan)
    for xi in x_right:
        try:
            y_right.append(f(xi))
        except ValueError:
            y_right.append(np.nan)

    plt.figure(figsize=(12, 8))
    plt.plot(x_left, y_left, 'r-', label='f(x)')
    plt.plot(x_right, y_right, 'r-')
    plt.xlim(-14, 20)
    plt.ylim(-6, 10)
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=2, color='r', linestyle='--', label='Asíntota (x=2)')
    plt.grid(True, alpha=0.3)
    if roots:
        for root in roots:
            if root is not None:
                plt.plot(root, 0, 'go', label=f'Raíz = {root:.2f}')
    if intervals:
        for a, b in intervals:
            plt.axvspan(a, b, alpha=0.2, color='gray')
    plt.grid(True)
    plt.legend()
    plt.title('Gráfica de f(x) = (4x - 7)/(x - 2)²')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()


def main() -> None:
    EPS = 1e-5
    roots = []
    intervals = [(1.5, 2.2), (1.5, 2.5)]

    # Caso a) intervalo [1.5, 2.2]
    try:
        start = time.time()
        root_a, iter_a, history_a = bisection_method(f, 1.5, 2.2, EPS, capture_history=True)
        end = time.time()
        print("(a) Bisección en [1.5, 2.2]")
        if history_a is not None:
            print_bisection_table("a", history_a)
        print(f"Raíz aproximada: {root_a:.9f}")
        print(f"Iteraciones: {iter_a}")
        print(f"Tiempo: {end - start:.9f} segundos\n")
        roots.append(root_a)
    except Exception as e:
        print(f"(a) Error: {e}\n")

    # Caso b) intervalo [1.5, 2.5]
    try:
        start = time.time()
        root_b, iter_b, history_b = bisection_method(f, 1.5, 2.5, EPS, capture_history=True)
        end = time.time()
        print("(b) Bisección en [1.5, 2.5]")
        if history_b is not None:
            print_bisection_table("b", history_b)
        print(f"Raíz aproximada: {root_b:.9f}")
        print(f"Iteraciones: {iter_b}")
        print(f"Tiempo: {end - start:.9f} segundos\n")
    except Exception as e:
        print(f"(b) Error: {e}\n")

    plot_function(roots=roots, intervals=intervals)


if __name__ == "__main__":
    main()
