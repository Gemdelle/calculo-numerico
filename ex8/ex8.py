"""
Unidad 2: Raíces de ecuaciones no lineales — Ejercicio 8
========================================================

Consigna:
- Calcule una aproximación del irracional √3 exacta a 10^{-4} usando el método de Newton para p0 = 2.
- Repita usando el método de la secante. Hacerlo en programas.
- Opcional: Trate de determinar con Series de Fourier y con Newton.

Este script resuelve x^2 − 3 = 0 con Newton y Secante e imprime las tablas.
"""

try:
	from common_functions import newton_method, secant_method, print_iteration_table
except ImportError:
	import os as _os
	import sys as _sys
	_sys.path.append(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
	from common_functions import newton_method, secant_method, print_iteration_table


def f(x: float) -> float:
    return x * x - 3.0


def df(x: float) -> float:
    return 2.0 * x


def main() -> None:
    tol = 1e-4

    root_newt, it_newt, tab_newt = newton_method(f, df, 2.0, tol=tol)
    print("Newton (p0=2.0):")
    print_iteration_table("Newton", tab_newt)
    print(f"Result: x≈{root_newt:.12f} in {it_newt} iterations\n")

    root_sec, it_sec, tab_sec = secant_method(f, 2.0, 1.5, tol=tol)
    print("Secante (p0=2.0, p1=1.5):")
    print_iteration_table("Secante", tab_sec)
    print(f"Result: x≈{root_sec:.12f} in {it_sec} iterations\n")


if __name__ == "__main__":
    main()
