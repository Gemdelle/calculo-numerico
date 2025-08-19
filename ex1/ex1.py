"""
Unidad 2: Raíces de ecuaciones no lineales — Ejercicio 1
========================================================

Consigna:
- Use el algoritmo de la bisección para encontrar las soluciones correctas a 10^{-5}
  para los siguientes problemas en 0 < x < 1:
  a) x − e^{-x} = 0       Respuesta esperada: x = 0.641181916
  b) e^{x} − x^2 + 3x − 2 = 0   Respuesta esperada: x = 0.257530212
- Hacer el ejercicio y reproducirlo con el programa.

Este script solicita p (1 a 15), ejecuta bisección y muestra la tabla de iteraciones.
"""

import math
import time
import sys

try:
	from common_functions import bisection_method, print_bisection_table
except ImportError:  # Permitir ejecución desde la subcarpeta
	import os as _os
	import sys as _sys
	_sys.path.append(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
	from common_functions import bisection_method, print_bisection_table


def f1(x: float) -> float:
	return x - math.exp(-x)


def f2(x: float) -> float:
	return math.exp(x) - x**2 + 3 * x - 2


def main() -> None:
	try:
		prec_exp = int(input("Ingrese un exponente p entre 1 y 15 (para 10^-p): "))
		if not (1 <= prec_exp <= 15):
			raise ValueError
	except ValueError:
		print("Por favor ingrese un exponente entero entre 1 y 15.")
		sys.exit(1)

	EPS = 10 ** (-prec_exp)

	cases = [
		("a", f1, 0.0, 1.0, "f1(x) = x - e^{-x}"),
		("b", f2, 0.0, 1.0, "f2(x) = e^{x} - x^2 + 3x - 2"),
	]

	for label, func, a, b, title in cases:
		print(f"\nBisección para {title}:")
		start = time.time()
		root, iters, history = bisection_method(func, a, b, tol=EPS, max_iter=1000, capture_history=True)
		end = time.time()
		if history is not None:
			print_bisection_table(label, history)
		print(f"\nRaíz encontrada: {root:.9f}")
		print(f"Iteraciones: {iters}")
		print(f"Tiempo de ejecución: {end - start:.9f} segundos")


if __name__ == "__main__":
	main()


