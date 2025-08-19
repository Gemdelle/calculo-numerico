def f(x):
    return x**3 - x - 1


a = 1
b = 2
tol = 1e-4
max_iter = 100

tabla = []  # Lista para almacenar las filas

for n in range(1, max_iter + 1):
    p = (a + b) / 2
    fp = f(p)
    error = (b - a) / 2

    # Guardar fila en la tabla
    tabla.append([n, a, b, p, fp, error])

    # Condición de parada
    if error < tol:
        break

    # Actualizar intervalo
    if f(a) * fp > 0:
        a = p
    else:
        b = p

# Imprimir tabla
print(f"{'n':<3} {'a':<10} {'b':<10} {'p':<10} {'f(p)':<15} {'(b-a)/2':<10}")
for fila in tabla:
    print(
        f"{fila[0]:<3} {fila[1]:<10.6f} {fila[2]:<10.6f} {fila[3]:<10.6f} {fila[4]:<15.10f} {fila[5]:<10.6f}"
    )
