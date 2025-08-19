import math


def newton(f, df, p0, tol=1e-4, max_iter=50):
    rows = []
    p = p0
    rows.append((0, p, f(p)))
    for n in range(1, max_iter + 1):
        fp = f(p)
        dfp = df(p)
        if dfp == 0:
            break
        p_new = p - fp / dfp
        rows.append((n, p_new, f(p_new), abs(p_new - p)))
        if abs(p_new - p) < tol:
            return p_new, n, rows
        p = p_new
    return p, n, rows


def secant(f, x0, x1, tol=1e-4, max_iter=50):
    rows = []
    f0 = f(x0)
    f1 = f(x1)
    rows.append((0, x0, f0))
    rows.append((1, x1, f1))
    for n in range(2, max_iter + 1):
        if (f1 - f0) == 0:
            break
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        rows.append((n, x2, f(x2), abs(x2 - x1)))
        if abs(x2 - x1) < tol:
            return x2, n, rows
        x0, f0 = x1, f1
        x1, f1 = x2, f(x2)
    return x1, n, rows


# Función para sqrt(3)
def f(x):
    return x * x - 3


def df(x):
    return 2 * x


tol = 1e-4

# Newton
root_newt, it_newt, tab_newt = newton(f, df, 2.0, tol=tol)
print("Newton (p0=2.0):")
for row in tab_newt:
    if len(row) == 3:
        print(f"n={row[0]:2d} x={row[1]:.12f} f={row[2]:.3e}")
    else:
        print(f"n={row[0]:2d} x={row[1]:.12f} f={row[2]:.3e} delta={row[3]:.3e}")
print(f"Result: x≈{root_newt:.12f} in {it_newt} iterations\n")

# Secant
root_sec, it_sec, tab_sec = secant(f, 2.0, 1.5, tol=tol)
print("Secant (p0=2.0, p1=1.5):")
for row in tab_sec:
    if len(row) == 3:
        print(f"n={row[0]:2d} x={row[1]:.12f} f={row[2]:.3e}")
    else:
        print(f"n={row[0]:2d} x={row[1]:.12f} f={row[2]:.3e} delta={row[3]:.3e}")
print(f"Result: x≈{root_sec:.12f} in {it_sec} iterations\n")
