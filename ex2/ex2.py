import time
import sys

"""
Ej 2: Determine cuantas iteraciones son necesarias para resolver x^3 + 4x^2 - 10 = 0 con una precisión ε=10^-5   Respuesta con 17 iteraciones.
"""

def f3(x):
    return x**3 + 4 * x**2 - 10

def bisection(func, a, b, tol, label):
    iter_count = 0
    print(f"{label}) Tabla de iteraciones")
    print(
        f"{'Iter':>4} | {'a':>17} | {'b':>17} | {'p=(a+b)/2':>17} | {'f(p)':>20} | {'(b-a)/2':>17}"
    )
    print("-" * 105)
    while True:
        c = (a + b) / 2.0
        fc = func(c)
        iter_count += 1

        print(
            f"{iter_count:4d} | {a:17.15f} | {b:17.15f} | {c:17.15f} | {fc:20.15e} | {(b - a) / 2:17.15f}"
        )

        if fc == 0 or (b - a) / 2 <= tol:
            break
        if fc < 0:
            a = c
        else:
            b = c
    return c, iter_count


def main():
    # if len(sys.argv) != 2:
    #     print(f"Uso: python {sys.argv[0]} <precision_exponente>")
    #     print("Ejemplo: python script.py 5  (para precisión 1e-5)")
    #     sys.exit(1)

    try:
        prec_exp = int(input("Ingrese un exponente entre 1 y 15: "))
        if not (1 <= prec_exp <= 15):
            raise ValueError
    except ValueError:
        print("Por favor ingrese un exponente entero entre 1 y 15.")
        sys.exit(1)

    EPS = 10 ** (-prec_exp)

    # Intervalo para la raíz de f3, suponemos entre 1 y 2 (porque f(1) = 1 + 4 - 10 = -5 < 0 y f(2) = 8 + 16 - 10 = 14 > 0)
    a3, b3 = 1.0, 2.0

    print("\nc) Bisección para f3 (x³ + 4x² - 10 = 0):\n")
    start = time.time()
    root3, iter3 = bisection(f3, a3, b3, EPS, "c")
    end = time.time()
    print(f"\nRaíz encontrada: {root3:.9f}")
    print(f"Iteraciones: {iter3}")
    print(f"Tiempo de ejecución: {end - start:.9f} segundos")


if __name__ == "__main__":
    main()
