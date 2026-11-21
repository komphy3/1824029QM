import numpy as np
import matplotlib.pyplot as plt
# Constants
hbar = 1.0
m = 1.0

# Half-width of well
a = 1.0

# Depth of potential well
V0 = 20.0
def k(E):
    return np.sqrt(2 * m * (E + V0)) / hbar
def kappa(E):
    return np.sqrt(-2 * m * E) / hbar
# Even-state equation
def even_equation(E):
    return k(E) * np.tan(k(E) * a) - kappa(E)
# Odd-state equation
def odd_equation(E):
    return -k(E) / np.tan(k(E) * a) - kappa(E)
def bisection(f, x1, x2, tolerance=1e-6):

    f1 = f(x1)
    f2 = f(x2)

    if f1 * f2 > 0:
        return None

    for i in range(100):

        xm = (x1 + x2) / 2
        fm = f(xm)

        if abs(fm) < tolerance:
            return xm

        if f1 * fm < 0:
            x2 = xm
            f2 = fm
        else:
            x1 = xm
            f1 = fm

    return (x1 + x2) / 2
E_values = np.linspace(-V0 + 0.01, -0.01, 10000)

even_energies = []
odd_energies = []

# Search for roots
for i in range(len(E_values) - 1):

    E1 = E_values[i]
    E2 = E_values[i + 1]
        f1 = even_equation(E1)
        f2 = even_equation(E2)

        if np.isfinite(f1) and np.isfinite(f2):
            if f1 * f2 < 0:
                root = bisection(even_equation, E1, E2)

                if root is not None:
                    if not any(abs(root - E) < 1e-4
                               for E in even_energies):
                        even_energies.append(root)
    except:
        pass

    try:
        f1 = odd_equation(E1)
        f2 = odd_equation(E2)

        if np.isfinite(f1) and np.isfinite(f2):
            if f1 * f2 < 0:
                root = bisection(odd_equation, E1, E2)

                if root is not None:
                    if not any(abs(root - E) < 1e-4
                               for E in odd_energies):
                        odd_energies.append(root)
    except:
        pass


# Combine all energy levels
energies = sorted(even_energies + odd_energies)

print("Energy Eigenvalues:")
for i, E in enumerate(energies):
    print(f"State {i + 1}: E = {E:.6f}")


# -----------------------------
# Plot potential well
# -----------------------------
x = np.linspace(-3 * a, 3 * a, 1000)

V = np.zeros_like(x)
V[np.abs(x) <= a] = -V0

plt.figure(figsize=(8, 5))

plt.plot(x, V, linewidth=2)

plt.axvline(-a, linestyle="--")
plt.axvline(a, linestyle="--")

plt.xlabel("x")
plt.ylabel("V(x)")
plt.title("Finite Potential Well")

plt.grid()
plt.show()
for n, E in enumerate(energies):

    k_value = k(E)
    kap_value = kappa(E)

    if is_even:

        psi = np.where(
            np.abs(x) <= a,
            np.cos(k_value * x),
            np.cos(k_value * a)
            * np.exp(-kap_value * (np.abs(x) - a))
        )

    else:

        psi = np.where(
            np.abs(x) <= a,
            np.sin(k_value * x),
            np.sign(x)
            * np.sin(k_value * a)
            * np.exp(-kap_value * (np.abs(x) - a))
        )

    # Normalize wavefunction
    dx = x[1] - x[0]

    norm = np.sqrt(np.sum(np.abs(psi)**2) * dx)

    psi = psi / norm

    plt.figure(figsize=(8, 5))

    plt.plot(x, psi)

    plt.axvline(-a, linestyle="--")
    plt.axvline(a, linestyle="--")

    plt.xlabel("x")
    plt.ylabel("ψ(x)")
    plt.title(
        f"Finite Well - State {n + 1}, E = {E:.4f}"
    )

    plt.grid()
    plt.show()
