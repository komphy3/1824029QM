import numpy as np
import matplotlib.pyplot as plt
hbar = 1.0
mass = 1.0
L = 1.0

# Number of grid points
N = 500
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# Use only interior points
x_inner = x[1:-1]
n = len(x_inne
# Potential energy
V = np.zeros(n)


# Hamiltonian matrix

# Kinetic energy coefficient
c = hbar**2 / (2 * mass * dx**2)

# Main diagonal
main_diagonal = 2 * c + V

# Upper and lower diagonals
off_diagonal = -c * np.ones(n - 1)

# Construct Hamiltonian matrix
H = (
    np.diag(main_diagonal)
    + np.diag(off_diagonal, 1)
    + np.diag(off_diagonal, -
# Numerical eigenvalues/eigenvectors
# --------------------------------
energy, wavefunction = np.linalg.eigh(H)
# Analytical energy
number_of_states = 4

analytical_energy = []

for k in range(1, number_of_states + 1):

    E = (k**2 * np.pi**2 * hbar**2) / (2 * mass * L**2)

    analytical_energy.append(E)



# Print comparison# 
print("Energy comparison")
print("-----------------------------")
print("n     Numerical       Analytical")

for k in range(number_of_states):

    print(
        f"{k+1}     "
        f"{energy[k]:.6f}     "
        f"{analytical_energy[k]:.6f}"

# Plot numerical wavefunctions

plt.figure(figsize=(8, 6))

for k in range(3):

    psi = wavefunction[:, k]

    # Normalize numerically
    norm = np.sqrt(np.sum(psi**2) * dx)
    psi = psi / norm

    plt.plot(
        x_inner,
        psi,
        label=f"n = {k+1}"
    )

plt.xlabel("Position x")
plt.ylabel("Wavefunction ψ(x)")
plt.title("Particle in a Box - Numerical Wavefunctions")
plt.legend()
plt.grid()

plt.show()


