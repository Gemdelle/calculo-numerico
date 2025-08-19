import math


def g(x):
    return (x - 1) ** 2 + x**4


def gp(x):
    return 4 * x**3 + 2 * x - 2  # g'(x)


def secant(f, x0, x1, tol=1e-4, max_iter=100):
    f0 = f(x0)
    f1 = f(x1)
    rows = [(0, x0, f0), (1, x1, f1)]
    for n in range(2, max_iter + 1):
        if (f1 - f0) == 0:
            break
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        rows.append((n, x2, f(x2), abs(x2 - x1)))
        if abs(x2 - x1) < tol:
            return x2, n, rows
        x0, f0 = x1, f1
        x1, f1 = x2, f(x2)
    return x1, max_iter, rows


x0, x1 = 0.0, 1.0
root, iters, table = secant(gp, x0, x1, tol=1e-4)

x_min = root
dist = math.hypot(x_min - 1, x_min**2)  # sqrt((x-1)^2 + x^4)

print("x_min =", x_min)
print("punto (x, x^2) =", (x_min, x_min**2))
print("distancia =", dist)
# puedes imprimir la tabla si querés:
for row in table:
    if len(row) == 3:
        print(row)
    else:
        print(row)
