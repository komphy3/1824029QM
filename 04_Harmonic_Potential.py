import numpy as np
import matplotlib.pyplot as plt

# --------------------------------
# Constants
# --------------------------------
hbar = 1.0
m = 1.0
omega = 1.0

# --------------------------------
# Numerical grid
# --------------------------------
N = 500
x_min = -8.0
x_max = 8.0

x = np.linspace(x_min, x_max, N)
dx = x[1] - x[0]

# Interior points
x_inner = x[1:-1]
n = len(x_inner)

# --------------------------------
# Harmonic potential
# --------------------------------
V = 0.5 * m * omega**2 * x_inner**2

# --------------------------------
# Kinetic energy coefficient
# --------------------------------
c = hbar**2 / (2 * m * dx**2)

# --------------------------------
# Hamiltonian matrix
# --------------------------------
main = 2 * c + V

off = -c * np.ones(n - 1)

H = (
    np.diag(main)
    + np.diag(off, 1)
    + np.diag(off, -1)
)

# --------------------------------
# Solve eigenvalue problem
# --------------------------------
energy, wavefunction = np.linalg.eigh(H)

# --------------------------------
# Analytical energies
# --------------------------------
number_of_states = 4

analytical_energy = []

for k in range(number_of_states):

    E = hbar * omega * (k + 0.5)

    analytical_energy.append(E)


# --------------------------------
# Print energy comparison
# --------------------------------
print("Harmonic Oscillator Energy")
print("--------------------------------")
print("n    Numerical     Analytical")

for k in range(number_of_states):

    print(
        f"{k}    "
        f"{energy[k]:.6f}     "
        f"{analytical_energy[k]:.6f}"
    )


# --------------------------------
# Plot potential
# --------------------------------
plt.figure(figsize=(8, 5))

plt.plot(x_inner, V)

plt.xlabel("x")
plt.ylabel("V(x)")
plt.title("Harmonic Oscillator Potential")

plt.grid()
plt.show()


# --------------------------------
# Plot wavefunctions
# --------------------------------
plt.figure(figsize=(8, 6))

for k in range(4):

    psi = wavefunction[:, k]

    # Normalize
    norm = np.sqrt(np.sum(psi**2) * dx)
    psi = psi / norm

    # Shift wavefunction to energy level
    psi_plot = psi + energy[k]

    plt.plot(
        x_inner,
        psi_plot,
        label=f"n = {k}"
    )

    # Energy level
    plt.axhline(
        energy[k],
        linestyle="--"
    )

plt.xlabel("x")
plt.ylabel("Energy / ψ(x)")
plt.title("Harmonic Oscillator Wavefunctions")

plt.legend()
plt.grid()
plt.show()



states = np.arange(number_of_states)

plt.figure(figsize=(8, 5))

plt.plot(
    states,
    energy[:number_of_states],
    "o-",
    label="Numerical"
)

plt.plot(
    states,
    analytical_energy,
    "s--",
    label="Analytical"
)

plt.xlabel("Quantum number n")
plt.ylabel("Energy")
plt.title("Numerical and Analytical Energies")

plt.legend()
plt.grid()
plt.show()
