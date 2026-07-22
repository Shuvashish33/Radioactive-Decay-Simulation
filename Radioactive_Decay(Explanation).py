import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Monte Carlo Simulation of Radioactive Decay
# --------------------------------------------------

# Fix the random number sequence (for reproducible results)
np.random.seed(0)

# Initial parameters
N0 = 1000          # Initial number of radioactive particles
lam = 0.1          # Probability of decay per time step
steps = 100        # Number of time steps

# Array to store the remaining number of particles
DK_MC = np.zeros(steps)

# Current number of particles
N = N0

# Monte Carlo simulation
for t in range(steps):

    # Count how many particles decay during this time step
    decays = np.sum(np.random.random(N) < lam)

    # Update the number of remaining particles
    N = N - decays

    # Store the remaining particles for plotting
    DK_MC[t] = N

# Time axis
t_axis = np.arange(steps)

# Exact analytical solution
DK_exact = N0 * np.exp(-lam * t_axis)

# --------------------------------------------------
# Plot the results
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    t_axis,
    DK_MC,
    'go',
    markersize=4,
    label="Monte Carlo Simulation"
)

plt.plot(
    t_axis,
    DK_exact,
    'r--',
    linewidth=2,
    label="Analytical Solution"
)

plt.title("Radioactive Decay: Monte Carlo vs Analytical Solution")
plt.xlabel("Time Step")
plt.ylabel("Remaining Particles")
plt.grid(True)
plt.legend()

plt.show()