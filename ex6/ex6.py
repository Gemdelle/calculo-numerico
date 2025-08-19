"""
Unidad 2: Raíces de ecuaciones no lineales — Ejercicio 6
========================================================

Consigna:
- Aproxime con 10^{-4} de precisión las siguientes ecuaciones siguiendo el método de Newton,
  y compare con los resultados del método de la secante. Obtenga resultados con un esquema gráfico
  y reprodúzcalos con un programa.

  1) x − cos(x) = 0   con [0, π/2]     Respuesta: p0 = 0.7854, p3 = 0.7390851
  2) x^3 + 3x^2 − 1 = 0   en [−4, 0]   Respuesta: p0 = −1, p3 = −0.65270365

Este programa implementa y compara Newton y Secante, imprime tablas de iteraciones y genera gráficos
de la función con raíces y de la convergencia de los métodos.
"""

import math
import numpy as np
import matplotlib.pyplot as plt
try:
	from common_functions import newton_method, secant_method, print_iteration_table
except ImportError:
	import os as _os
	import sys as _sys
	_sys.path.append(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
	from common_functions import newton_method, secant_method, print_iteration_table

# Configuración general
TOLERANCE = 1e-4  # Tolerancia para convergencia
MAX_ITERATIONS = 50  # Máximo número de iteraciones permitidas


def plot_function_and_roots(f, x_range, roots, methods, iterations, title, problem_num):
    """
    Genera un gráfico de la función y las raíces encontradas por los métodos numéricos.

    Argumentos:
        f (function): La función a graficar
        x_range (list): [x_min, x_max] para el rango de visualización
        roots (list): Lista de raíces encontradas
        methods (list): Nombres de los métodos usados
        iterations (list): Número de iteraciones para cada método
        title (str): Título del gráfico
        problem_num (int): Número del problema
    """
    # Genera puntos para graficar la función
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = [f(xi) for xi in x]

    # Configura el tamaño y crea la figura
    plt.figure(figsize=(12, 7))

    # Grafica la función y el eje x
    plt.plot(x, y, 'b-', label='f(x)')
    plt.plot(x, np.zeros_like(x), 'k--', alpha=0.3)  # eje x

    # Agrega las raíces con etiquetas específicas
    colors = ['r', 'g']  # Colores para cada método
    for i, (root, method, iters) in enumerate(zip(roots, methods, iterations)):
        plt.plot(root, 0, f'{colors[i]}o',
                 label=f'{method}: x ≈ {root:.7f} ({iters} iteraciones)')

    # Configura la apariencia del gráfico
    plt.grid(True, alpha=0.3)
    plt.title(f'Análisis de Raíces: {title}', pad=20, size=12)
    plt.suptitle(f'Búsqueda de Raíces - Problema {problem_num}', size=14)
    plt.xlabel('x')
    plt.ylabel('f(x)')

    # Ajusta la leyenda y muestra el gráfico
    plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=2)
    plt.tight_layout()
    plt.show()

def plot_convergence(rows_newton, rows_secant, title, problem_num):
    """
    Genera un gráfico comparativo de la convergencia de los métodos.

    Argumentos:
        rows_newton (list): Historial de iteraciones del método de Newton
        rows_secant (list): Historial de iteraciones del método de la Secante
        title (str): Título del gráfico
        problem_num (int): Número del problema
    """
    plt.figure(figsize=(12, 7))

    # Extrae los valores de error para el método de Newton
    n_newton = []
    errors_newton = []
    for i, row in enumerate(rows_newton):
        n_newton.append(i)
        if len(row) > 3:
            errors_newton.append(row[3])  # Usa el error calculado si está disponible
        elif i > 0:
            # Calcula el error como la diferencia entre iteraciones consecutivas
            errors_newton.append(abs(row[1] - rows_newton[i-1][1]))

    # Extrae los valores de error para el método de la Secante
    n_secant = []
    errors_secant = []
    for i, row in enumerate(rows_secant):
        n_secant.append(i)
        if len(row) > 3:
            errors_secant.append(row[3])  # Usa el error calculado si está disponible
        elif i > 0:
            # Calcula el error como la diferencia entre iteraciones consecutivas
            errors_secant.append(abs(row[1] - rows_secant[i-1][1]))

    # Grafica los errores en escala logarítmica (omitir la iteración 0)
    plt.semilogy(n_newton[1:], errors_newton[1:], 'bo-',
                 label=f'Newton (convergencia en {len(errors_newton) - 1} pasos)')
    plt.semilogy(n_secant[1:], errors_secant[1:], 'ro-',
                 label=f'Secante (convergencia en {len(errors_secant) - 1} pasos)')

    # Configura la apariencia del gráfico
    plt.grid(True, alpha=0.3)
    plt.title(f'Análisis de Convergencia: {title}', pad=20, size=12)
    plt.suptitle(f'Velocidad de Convergencia - Problema {problem_num}', size=14)
    plt.xlabel('Número de Iteración')
    plt.ylabel('Error (escala logarítmica)')

    # Agrega información sobre el error final
    final_error_newton = errors_newton[-1]
    final_error_secant = errors_secant[-1]
    info_text = f'Error final:\nNewton: {final_error_newton:.2e}\nSecante: {final_error_secant:.2e}'
    plt.text(0.02, 0.02, info_text, transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', alpha=0.8), fontsize=9)

    # Ajusta la leyenda y muestra el gráfico
    plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=2)
    plt.tight_layout()
    plt.show()

def print_table(title, rows):
    # Mantener compatibilidad pero delegar al helper común
    print_iteration_table(title, rows)


# =============================================================================
# Definición de problemas
# =============================================================================

class Problem1:
    """Problema 1: f(x) = x - cos(x)"""

    @staticmethod
    def f(x):
        """Función objetivo: f(x) = x - cos(x)"""
        return x - math.cos(x)

    @staticmethod
    def df(x):
        """Derivada de la función: f'(x) = 1 + sin(x)"""
        return 1 + math.sin(x)

    # Parámetros iniciales
    newton_p0 = 0.7854  # π/4 aproximadamente
    secant_x0 = 0.0
    secant_x1 = math.pi / 2
    plot_range = [0, 2]
    title = "f(x) = x - cos(x)"


class Problem2:
    """Problema 2: f(x) = x³ + 3x² - 1"""

    @staticmethod
    def f(x):
        """Función objetivo: f(x) = x³ + 3x² - 1"""
        return x**3 + 3 * x**2 - 1

    @staticmethod
    def df(x):
        """Derivada de la función: f'(x) = 3x² + 6x"""
        return 3 * x**2 + 6 * x

    # Parámetros iniciales
    newton_p0 = -1.0
    secant_x0 = -1.0
    secant_x1 = -0.5  # Más cerca de la raíz negativa
    plot_range = [-2, 1]
    title = "f(x) = x³ + 3x² - 1"


def solve_and_plot(problem, problem_num):
    """
    Resuelve un problema usando ambos métodos y muestra los resultados.

    Argumentos:
        problem: Clase que define el problema (Problem1 o Problem2)
        problem_num: Número del problema para los títulos
    """
    # Resolver usando el método de Newton
    root_n, it_n, tab_n = newton_method(problem.f, problem.df, problem.newton_p0, tol=TOLERANCE, max_iter=MAX_ITERATIONS)

    # Resolver usando el método de la Secante
    root_s, it_s, tab_s = secant_method(problem.f, problem.secant_x0, problem.secant_x1, tol=TOLERANCE, max_iter=MAX_ITERATIONS)

    # Mostrar resultados en tablas
    print_table(f"Newton: {problem.title}, p0={problem.newton_p0}", tab_n)
    print(f"Newton result: x ≈ {root_n:.7f} in {it_n} iterations\n")

    print_table(f"Secant: {problem.title}, x0={problem.secant_x0}, x1={problem.secant_x1}", tab_s)
    print(f"Secant result: x ≈ {root_s:.7f} in {it_s} iterations\n")

    # Visualizar resultados
    plot_function_and_roots(problem.f, problem.plot_range,
                            [root_n, root_s], ["Newton", "Secante"],
                            [it_n, it_s], problem.title, problem_num)

    plot_convergence(tab_n, tab_s, problem.title, problem_num)


# =============================================================================
# Ejecución principal
# =============================================================================

if __name__ == "__main__":
    print("\nResolviendo Problema 1...")
    print("=" * 50)
    solve_and_plot(Problem1, 1)

    print("\nResolviendo Problema 2...")
    print("=" * 50)
    solve_and_plot(Problem2, 2)
