"""
Funciones comunes para los ejercicios de Cálculo Numérico.

Incluye implementaciones genéricas de:
- Método de Bisección (con historial opcional)
- Método de Newton-Raphson (con historial)
- Método de la Secante (con historial)
- Utilidades para imprimir tablas de iteraciones
"""

from typing import Callable, List, Tuple, Optional


# =============================================================================
# Métodos de búsqueda de raíces
# =============================================================================

def bisection_method(
	func: Callable[[float], float],
	a: float,
	b: float,
	tol: float = 1e-5,
	max_iter: int = 1000,
	capture_history: bool = True,
) -> Tuple[float, int, Optional[List[Tuple[int, float, float, float, float, float]]]]:
	"""
	Método de la Bisección para localizar una raíz en [a, b].

	Retorna (raíz_aprox, num_iter, historial) donde historial, si se captura,
	es una lista de tuplas: (n, a, b, p, f(p), (b-a)/2).
	"""
	fa = func(a)
	fb = func(b)
	if fa * fb > 0:
		raise ValueError("La función no cambia de signo en el intervalo dado")

	history: Optional[List[Tuple[int, float, float, float, float, float]]] = [] if capture_history else None
	iter_count = 0

	while (b - a) / 2.0 > tol and iter_count < max_iter:
		p = (a + b) / 2.0
		fp = func(p)
		iter_count += 1
		if capture_history and history is not None:
			history.append((iter_count, a, b, p, fp, (b - a) / 2.0))
		if fp == 0:
			break
		if fa * fp < 0:
			b = p
			fb = fp
		else:
			a = p
			fa = fp

	return (a + b) / 2.0, iter_count, history


def newton_method(
	f: Callable[[float], float],
	df: Callable[[float], float],
	p0: float,
	tol: float = 1e-4,
	max_iter: int = 50,
) -> Tuple[float, int, List[Tuple[int, float, float, float]]]:
	"""
	Método de Newton-Raphson con historial de iteraciones.

	Retorna (raíz, iteraciones, historial) donde historial contiene
	(n, x_n, f(x_n), delta) y la primera fila es (0, p0, f(p0)).
	"""
	rows: List[Tuple[int, float, float, float]] = []
	p = p0
	rows.append((0, p, f(p), 0.0))
	for n in range(1, max_iter + 1):
		fp = f(p)
		dfp = df(p)
		if dfp == 0:
			break
		p_new = p - fp / dfp
		delta = abs(p_new - p)
		rows.append((n, p_new, f(p_new), delta))
		if delta < tol:
			return p_new, n, rows
		p = p_new
	return p, n, rows


def secant_method(
	f: Callable[[float], float],
	x0: float,
	x1: float,
	tol: float = 1e-4,
	max_iter: int = 50,
) -> Tuple[float, int, List[Tuple[int, float, float, float]]]:
	"""
	Método de la Secante con historial de iteraciones.

	Retorna (raíz, iteraciones, historial) donde historial contiene
	(n, x_n, f(x_n), delta) y las dos primeras filas corresponden a x0 y x1.
	"""
	rows: List[Tuple[int, float, float, float]] = []
	f0 = f(x0)
	f1 = f(x1)
	rows.append((0, x0, f0, 0.0))
	rows.append((1, x1, f1, abs(x1 - x0)))
	for n in range(2, max_iter + 1):
		if (f1 - f0) == 0:
			break
		x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
		delta = abs(x2 - x1)
		rows.append((n, x2, f(x2), delta))
		if delta < tol:
			return x2, n, rows
		x0, f0 = x1, f1
		x1, f1 = x2, f(x2)
	return x2, n-1, rows


# =============================================================================
# Impresión de tablas
# =============================================================================

def print_iteration_table(title: str, rows: List[Tuple[int, float, float, float]]) -> None:
	"""Imprime una tabla genérica para métodos iterativos (Newton/Secante)."""
	print("\n" + title)
	print(f"{'n':>2} {'x':>14} {'f(x)':>15} {'delta':>12}")
	print("-" * 45)
	for n, x, fx, delta in rows:
		if n == 0:
			print(f"{n:2d} {x:14.7f} {fx:15.7e} {'':12}")
		else:
			print(f"{n:2d} {x:14.7f} {fx:15.7e} {delta:12.7e}")
	print("-" * 45)


def print_bisection_table(label: str, history: List[Tuple[int, float, float, float, float, float]]) -> None:
	"""
	Imprime la tabla de bisección con columnas: n, a, b, p, f(p), (b-a)/2.
	"""
	print(f"{label}) Tabla de iteraciones")
	print(f"{'Iter':>4} | {'a':>17} | {'b':>17} | {'p=(a+b)/2':>17} | {'f(p)':>20} | {'(b-a)/2':>17}")
	print("-" * 105)
	for (n, a, b, p, fp, half_width) in history:
		print(f"{n:4d} | {a:17.15f} | {b:17.15f} | {p:17.15f} | {fp:20.15e} | {half_width:17.15f}")


