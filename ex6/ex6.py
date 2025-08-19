"""
Ejercicio 6: Implementación y Comparación de Métodos Numéricos
=============================================================

Este programa implementa y compara los métodos de Newton-Raphson y Secante
para encontrar raíces de funciones no lineales. Se analizan dos problemas:

Problema 1: f(x) = x - cos(x)
Problema 2: f(x) = x³ + 3x² - 1

Para cada problema, se calculan las raíces usando ambos métodos y se visualizan:
- La función y las raíces encontradas
- La convergencia de cada método
- Tablas con los resultados numéricos
"""

import math
import numpy as np
import matplotlib.pyplot as plt

# Configuración general
TOLERANCE = 1e-4  # Tolerancia para convergencia
MAX_ITERATIONS = 50  # Máximo número de iteraciones permitidas


def newton(f, df, p0, tol=TOLERANCE, max_iter=MAX_ITERATIONS):
    """
    Implementa el método de Newton-Raphson para encontrar raíces.

    Argumentos:
        f (function): La función cuya raíz se busca
        df (function): La derivada de la función f
        p0 (float): Punto inicial para comenzar la búsqueda
        tol (float): Tolerancia para el criterio de convergencia
        max_iter (int): Número máximo de iteraciones permitidas

    Retorna:
        tuple: (raíz encontrada, número de iteraciones, historial de iteraciones)
    """
    rows = []  # Almacena el historial de iteraciones
    p = p0
    rows.append((0, p, f(p)))  # Guarda el punto inicial

    for n in range(1, max_iter + 1):
        fp = f(p)
        dfp = df(p)

        # Verifica si la derivada es cero para evitar división por cero
        if dfp == 0:
            break

        # Calcula el siguiente punto usando la fórmula de Newton
        p_new = p - fp / dfp
        rows.append((n, p_new, f(p_new), abs(p_new - p)))

        # Verifica convergencia
        if abs(p_new - p) < tol:
            return p_new, n, rows

        p = p_new

    return p, n, rows


def secant(f, x0, x1, tol=TOLERANCE, max_iter=MAX_ITERATIONS):
    """
    Implementa el método de la Secante para encontrar raíces.

    Argumentos:
        f (function): La función cuya raíz se busca
        x0 (float): Primer punto inicial
        x1 (float): Segundo punto inicial
        tol (float): Tolerancia para el criterio de convergencia
        max_iter (int): Número máximo de iteraciones permitidas

    Retorna:
        tuple: (raíz encontrada, número de iteraciones, historial de iteraciones)
    """
    rows = []  # Almacena el historial de iteraciones
    f0 = f(x0)
    f1 = f(x1)
    rows.append((0, x0, f0))  # Guarda el primer punto inicial
    rows.append((1, x1, f1))  # Guarda el segundo punto inicial

    for n in range(2, max_iter + 1):
        # Verifica si la pendiente es cero para evitar división por cero
        if (f1 - f0) == 0:
            break

        # Calcula el siguiente punto usando la fórmula de la Secante
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        rows.append((n, x2, f(x2), abs(x2 - x1)))

        # Verifica convergencia
        if abs(x2 - x1) < tol:
            return x2, n, rows

        # Actualiza los puntos para la siguiente iteración
        x0, f0 = x1, f1
        x1, f1 = x2, f(x2)

    return x1, n, rows


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

    # Grafica los errores en escala logarítmica
    plt.semilogy(n_newton[1:], errors_newton, 'bo-',
                 label=f'Newton (convergencia en {len(errors_newton)} pasos)')
    plt.semilogy(n_secant[1:], errors_secant, 'ro-',
                 label=f'Secante (convergencia en {len(errors_secant)} pasos)')

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
    """
    Imprime una tabla formateada con los resultados de las iteraciones.

    Argumentos:
        title (str): Título de la tabla
        rows (list): Lista de tuplas con los datos de cada iteración
    """
    print("\n" + title)
    print(f"{'n':>2} {'x':>14} {'f(x)':>15} {'delta':>12}")
    print("-" * 45)  # Línea separadora

    for r in rows:
        if len(r) == 3:
            # Primera iteración (sin delta)
            print(f"{r[0]:2d} {r[1]:14.7f} {r[2]:15.7e} {'':12}")
        else:
            # Iteraciones subsiguientes (con delta)
            print(f"{r[0]:2d} {r[1]:14.7f} {r[2]:15.7e} {r[3]:12.7e}")
    print("-" * 45)  # Línea separadora


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
    root_n, it_n, tab_n = newton(problem.f, problem.df, problem.newton_p0)

    # Resolver usando el método de la Secante
    root_s, it_s, tab_s = secant(problem.f, problem.secant_x0, problem.secant_x1)

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
