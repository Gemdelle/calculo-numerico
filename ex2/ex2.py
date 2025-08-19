"""
Unidad 2: Raíces de ecuaciones no lineales — Ejercicio 2
========================================================

Consigna:
- Determine cuántas iteraciones son necesarias para resolver x^3 + 4x^2 − 10 = 0
  con una precisión ε = 10^{-5}. Respuesta: 17 iteraciones.
- Hacer el ejercicio y reproducirlo con el programa.

Este script aplica bisección en [1, 2] y muestra la tabla de iteraciones.
"""

import time
import sys

try:
	from common_functions import bisection_method, print_bisection_table
except ImportError:
	import os as _os
	import sys as _sys
	_sys.path.append(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
	from common_functions import bisection_method, print_bisection_table


def f3(x: float) -> float:
    return x**3 + 4 * x**2 - 10


def main() -> None:
    try:
        prec_exp = int(input("Ingrese un exponente p entre 1 y 15 (para 10^-p): "))
        if not (1 <= prec_exp <= 15):
            raise ValueError
    except ValueError:
        print("Por favor ingrese un exponente entero entre 1 y 15.")
        sys.exit(1)

    EPS = 10 ** (-prec_exp)

    a3, b3 = 1.0, 2.0
    print("\nBisección para f3 (x³ + 4x² - 10 = 0):\n")
    start = time.time()
    root3, iter3, history = bisection_method(f3, a3, b3, tol=EPS, max_iter=1000, capture_history=True)
    end = time.time()
    if history is not None:
        print_bisection_table("c", history)
    print(f"\nRaíz encontrada: {root3:.9f}")
    print(f"Iteraciones: {iter3}")
    print(f"Tiempo de ejecución: {end - start:.9f} segundos")


if __name__ == "__main__":
    main()
