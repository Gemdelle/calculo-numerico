"""
Unidad 2: Raíces de ecuaciones no lineales — Ejercicio 5
========================================================

Consigna:
- Use el Teorema (2.1) para encontrar una cota al número de iteraciones necesarias
  para alcanzar una aproximación con exactitud de 10^{-4} a la solución de x^3 − x − 1 = 0
  en [1, 2]. Encuentre una aproximación a la raíz con este grado de exactitud.
  Respuesta: 14.1324768. Reproducir con un programa.

Este script aplica bisección en [1, 2] y muestra la tabla de iteraciones.
"""

try:
	from common_functions import bisection_method, print_bisection_table
except ImportError:
	import os as _os
	import sys as _sys
	_sys.path.append(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
	from common_functions import bisection_method, print_bisection_table


def f(x: float) -> float:
    return x**3 - x - 1


def main() -> None:
    a, b = 1.0, 2.0
    tol = 1e-4
    root, iters, history = bisection_method(f, a, b, tol=tol, capture_history=True)
    print_bisection_table("a", history or [])
    print(f"\nRaíz ≈ {root:.9f} | Iteraciones: {iters}")


if __name__ == "__main__":
    main()
