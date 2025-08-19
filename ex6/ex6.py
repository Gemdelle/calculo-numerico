import math
import numpy as np
import matplotlib.pyplot as plt


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


def plot_function_and_roots(f, x_range, roots, methods, iterations, title, problem_num):
    x = np.linspace(x_range[0], x_range[1], 1000)
    y = [f(xi) for xi in x]
    
    plt.figure(figsize=(12, 7))
    plt.plot(x, y, 'b-', label='f(x)')
    plt.plot(x, np.zeros_like(x), 'k--', alpha=0.3)  # x-axis
    
    # Agregar las raíces con etiquetas específicas
    colors = ['r', 'g']
    for i, (root, method, iters) in enumerate(zip(roots, methods, iterations)):
        plt.plot(root, 0, f'{colors[i]}o', 
                label=f'{method}: x ≈ {root:.7f} ({iters} iteraciones)')
    
    plt.grid(True, alpha=0.3)
    plt.title(f'Análisis de Raíces: {title}', pad=20, size=12)
    plt.suptitle(f'Búsqueda de Raíces - Problema {problem_num}', size=14)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=2)
    plt.tight_layout()
    plt.show()

def plot_convergence(rows_newton, rows_secant, title, problem_num):
    plt.figure(figsize=(12, 7))
    
    # Extract error values (delta) from rows
    n_newton = []
    errors_newton = []
    for i, row in enumerate(rows_newton):
        n_newton.append(i)
        if len(row) > 3:
            errors_newton.append(row[3])
        elif i > 0:
            errors_newton.append(abs(row[1] - rows_newton[i-1][1]))
    
    n_secant = []
    errors_secant = []
    for i, row in enumerate(rows_secant):
        n_secant.append(i)
        if len(row) > 3:
            errors_secant.append(row[3])
        elif i > 0:
            errors_secant.append(abs(row[1] - rows_secant[i-1][1]))
    
    plt.semilogy(n_newton[1:], errors_newton, 'bo-', 
                 label=f'Newton (convergencia en {len(errors_newton)} pasos)')
    plt.semilogy(n_secant[1:], errors_secant, 'ro-', 
                 label=f'Secante (convergencia en {len(errors_secant)} pasos)')
    
    plt.grid(True, alpha=0.3)
    plt.title(f'Análisis de Convergencia: {title}', pad=20, size=12)
    plt.suptitle(f'Velocidad de Convergencia - Problema {problem_num}', size=14)
    plt.xlabel('Número de Iteración')
    plt.ylabel('Error (escala logarítmica)')
    
    # Agregar información sobre el error final
    final_error_newton = errors_newton[-1]
    final_error_secant = errors_secant[-1]
    info_text = f'Error final:\nNewton: {final_error_newton:.2e}\nSecante: {final_error_secant:.2e}'
    plt.text(0.02, 0.02, info_text, transform=plt.gca().transAxes, 
             bbox=dict(facecolor='white', alpha=0.8), fontsize=9)
    
    plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=2)
    plt.tight_layout()
    plt.show()

def print_table(title, rows):
    print("\n" + title)
    print(f"{'n':>2} {'x':>14} {'f(x)':>15} {'delta':>12}")
    for r in rows:
        if len(r) == 3:
            print(f"{r[0]:2d} {r[1]:14.7f} {r[2]:15.7e} {'':12}")
        else:
            print(f"{r[0]:2d} {r[1]:14.7f} {r[2]:15.7e} {r[3]:12.7e}")


# --- Problema 1
def f1(x):
    return x - math.cos(x)


def df1(x):
    return 1 + math.sin(x)


p0_1 = 0.7854
root_n1, it_n1, tab_n1 = newton(f1, df1, p0_1)
root_s1, it_s1, tab_s1 = secant(f1, 0.0, math.pi / 2)

print_table("Newton: f(x)=x-cos(x), p0=0.7854", tab_n1)
print(f"Newton result: x ≈ {root_n1:.7f} in {it_n1} iterations\n")
print_table("Secant: f(x)=x-cos(x), x0=0, x1=pi/2", tab_s1)
print(f"Secant result: x ≈ {root_s1:.7f} in {it_s1} iterations\n")

# Visualizar función y raíces para el Problema 1
plot_function_and_roots(f1, [0, 2], [root_n1, root_s1], 
                       ["Newton", "Secante"], [it_n1, it_s1],
                       "f(x) = x - cos(x)", 1)
plot_convergence(tab_n1, tab_s1, "f(x) = x - cos(x)", 1)


# --- Problema 2
def f2(x):
    return x**3 + 3 * x**2 - 1


def df2(x):
    return 3 * x**2 + 6 * x


p0_2 = -1.0
root_n2, it_n2, tab_n2 = newton(f2, df2, p0_2)
# secante: mejor usar x0=-1, x1=-0.5 (más cerca de la raíz negativa)
root_s2, it_s2, tab_s2 = secant(f2, -1.0, -0.5)

print_table("Newton: f(x)=x^3+3x^2-1, p0=-1", tab_n2)
print(f"Newton result: x ≈ {root_n2:.8f} in {it_n2} iterations\n")
print_table("Secant: f(x)=x^3+3x^2-1, x0=-1, x1=-0.5", tab_s2)
print(f"Secant result: x ≈ {root_s2:.8f} in {it_s2} iterations\n")

# Visualizar función y raíces para el Problema 2
plot_function_and_roots(f2, [-2, 1], [root_n2, root_s2],
                       ["Newton", "Secante"], [it_n2, it_s2],
                       "f(x) = x³ + 3x² - 1", 2)
plot_convergence(tab_n2, tab_s2, "f(x) = x³ + 3x² - 1", 2)
