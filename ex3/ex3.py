import math
import time


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


def main():
    EPS = 1e-5

    # Caso a) intervalo [1.5, 2.2]
    try:
        start = time.time()
        root_a, iter_a = bisection(f, 1.5, 2.2, EPS)
        end = time.time()
        print(f"(a) Raíz aproximada: {root_a:.9f}")
        print(f"    Iteraciones: {iter_a}")
        print(f"    Tiempo: {end - start:.9f} segundos\n")
    except Exception as e:
        print(f"(a) Error: {e}\n")

    # Caso b) intervalo [1.5, 2.5]
    try:
        start = time.time()
        root_b, iter_b = bisection(f, 1.5, 2.5, EPS)
        end = time.time()
        print(f"(b) Raíz aproximada: {root_b:.9f}")
        print(f"    Iteraciones: {iter_b}")
        print(f"    Tiempo: {end - start:.9f} segundos\n")
    except Exception as e:
        print(f"(b) Error: {e}\n")


if __name__ == "__main__":
    main()
