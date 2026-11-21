import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm

# Values of l and m
l = 2
m = 1

# Angular coordinates
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)

theta, phi = np.meshgrid(theta, phi)

# Spherical harmonic
Y = sph_harm(m, l, phi, theta)

# Probability density
probability = np.abs(Y)**2

# Convert spherical coordinates to Cartesian coordinates
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

# Plot probability density on sphere
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(
    x, y, z,
    facecolors=plt.cm.viridis(probability / probability.max())
)

ax.set_title(f"Spherical Harmonic: l = {l}, m = {m}")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()
