"""
Unidad 2: Raíces de ecuaciones no lineales — Ejercicio 7
========================================================

Consigna:
- Use el método de Newton para aproximar con 10^{-4} el valor de x que produce un punto
  de la gráfica y = x^2 más cercano a (1, 0). Minimice d(x)^2 donde d(x) es la distancia
  entre (x, x^2) y (1, 0). Hacerlo con Regula Falsi o método de la secante.

Este script minimiza g(x) = (x − 1)^2 + x^4 encontrando g'(x) = 0 con secante.
"""

import math
try:
	from common_functions import secant_method, print_iteration_table
except ImportError:
	import os as _os
	import sys as _sys
	_sys.path.append(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
	from common_functions import secant_method, print_iteration_table


def g(x: float) -> float:
    return (x - 1) ** 2 + x**4


def gp(x: float) -> float:
    return 4 * x**3 + 2 * x - 2


def main() -> None:
    x0, x1 = 0.0, 1.0
    root, iters, table = secant_method(gp, x0, x1, tol=1e-4)
    x_min = root
    dist = math.hypot(x_min - 1, x_min**2)

    print(f"x_min = {x_min}")
    print(f"punto (x, x^2) = ({x_min}, {x_min**2})")
    print(f"distancia = {dist}")
    print_iteration_table("Secante sobre g'(x)", table)


if __name__ == "__main__":
    main()
