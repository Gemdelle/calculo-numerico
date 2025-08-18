import math
import time
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    if x == 2:
        # Evitar división por cero
        raise ValueError("f(x) no está definida en x=2")
    return (4 * x - 7) / ((x - 2) ** 2)


def safe_eval(func, x):
    try:
        return func(x)
    except ValueError:
        return None  # Indica función no definida


def bisection(func, a, b, tol, max_iter=1000):
    iter_count = 0
    fa = safe_eval(func, a)
    fb = safe_eval(func, b)
    if fa is None or fb is None:
        raise ValueError("La función no está definida en los extremos del intervalo")

    if fa * fb > 0:
        raise ValueError(
            "La función no cambia de signo en el intervalo, bisección no es aplicable"
        )

    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        fc = safe_eval(func, c)
        if fc is None:
            # Punto no definido, romper para evitar error
            break
        iter_count += 1
        if fc == 0 or (b - a) / 2 < tol:
            return c, iter_count
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2, iter_count


def plot_function(roots=None, intervals=None):
    # Crear puntos para graficar
    x_left = np.linspace(-14, 1.9, 1000)  # Puntos a la izquierda de la asíntota
    x_right = np.linspace(2.1, 20, 1000)  # Puntos a la derecha de la asíntota
    
    # Calcular valores para ambos lados de la asíntota
    y_left = []
    y_right = []
    
    for xi in x_left:
        try:
            yi = f(xi)
            y_left.append(yi)
        except ValueError:
            y_left.append(np.nan)
            
    for xi in x_right:
        try:
            yi = f(xi)
            y_right.append(yi)
        except ValueError:
            y_right.append(np.nan)
    
    # Crear la gráfica
    plt.figure(figsize=(12, 8))
    plt.plot(x_left, y_left, 'r-', label='f(x)')
    plt.plot(x_right, y_right, 'r-')
    
    # Ajustar límites y escala
    plt.xlim(-14, 20)
    plt.ylim(-6, 10)
    
    # Agregar ejes y cuadrícula
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=2, color='r', linestyle='--', label='Asíntota (x=2)')
    plt.grid(True, alpha=0.3)
    
    # Agregar raíces si existen
    if roots:
        for root in roots:
            if root is not None:
                plt.plot(root, 0, 'go', label=f'Raíz = {root:.2f}')
    
    # Agregar intervalos si existen
    if intervals:
        for a, b in intervals:
            plt.axvspan(a, b, alpha=0.2, color='gray')
    
    plt.grid(True)
    plt.legend()
    plt.title('Gráfica de f(x) = (4x - 7)/(x - 2)²')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

def main():
    EPS = 1e-5
    roots = []
    intervals = [(1.5, 2.2), (1.5, 2.5)]

    # Caso a) intervalo [1.5, 2.2]
    try:
        start = time.time()
        root_a, iter_a = bisection(f, 1.5, 2.2, EPS)
        end = time.time()
        print(f"(a) Raíz aproximada: {root_a:.9f}")
        print(f"    Iteraciones: {iter_a}")
        print(f"    Tiempo: {end - start:.9f} segundos\n")
        roots.append(root_a)
    except Exception as e:
        print(f"(a) Error: {e}\n")

    # Graficar la función con las raíces e intervalos encontrados
    plot_function(roots=roots, intervals=intervals)


if __name__ == "__main__":
    main()
