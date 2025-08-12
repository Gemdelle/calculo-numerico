import math
import time
import sys


def f1(x):
    return x - math.exp(-x)


def f2(x):
    return math.exp(x) - x**2 + 3 * x - 2


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
        if func(a) * fc < 0:
            b = c
        else:
            a = c
    return c, iter_count


def main():
    if len(sys.argv) != 2:
        print(f"Uso: python {sys.argv[0]} <precision_exponente>")
        print("Ejemplo: python script.py 5  (para precisión 1e-5)")
        sys.exit(1)

    try:
        prec_exp = int(sys.argv[1])
        if not (1 <= prec_exp <= 15):
            raise ValueError
    except ValueError:
        print("Por favor ingrese un exponente entero entre 1 y 15.")
        sys.exit(1)

    EPS = 10 ** (-prec_exp)

    a1, b1 = 0.0, 1.0
    a2, b2 = 0.0, 1.0

    print("\nBisección para f1 (x - e^-x = 0):\n")
    start = time.time()
    root1, iter1 = bisection(f1, a1, b1, EPS, "a")
    end = time.time()
    print(f"\nRaíz encontrada: {root1:.9f}")
    print(f"Iteraciones: {iter1}")
    print(f"Tiempo de ejecución: {end - start:.9f} segundos\n")

    print("\nBisección para f2 (e^x - x^2 + 3x - 2 = 0):\n")
    start = time.time()
    root2, iter2 = bisection(f2, a2, b2, EPS, "b")
    end = time.time()
    print(f"\nRaíz encontrada: {root2:.9f}")
    print(f"Iteraciones: {iter2}")
    print(f"Tiempo de ejecución: {end - start:.9f} segundos")


if __name__ == "__main__":
    main()
