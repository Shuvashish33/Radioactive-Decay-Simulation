# Radioactive Decay Simulation

## Overview

This project simulates radioactive decay using the Monte Carlo method in Python. Each radioactive particle is assigned a fixed probability of decay during every time step. The simulation is then compared with the exact analytical solution of the exponential decay law.

This project was developed as part of my Computational Physics learning journey.

---

## Physics Background

Radioactive decay is a stochastic process in which unstable nuclei decay randomly over time.

The analytical solution is

\[
N(t)=N_0e^{-\lambda t}
\]

where

- \(N_0\) = Initial number of particles
- \(\lambda\) = Decay constant
- \(N(t)\) = Remaining particles after time \(t\)

The Monte Carlo simulation approximates this process by generating random numbers for every particle at each time step.

---

## Features

- Monte Carlo simulation using NumPy
- Random decay of individual particles
- Comparison with the analytical exponential decay equation
- Visualization using Matplotlib
- Reproducible results using a fixed random seed

---

## Technologies Used

- Python
- NumPy
- Matplotlib

---

## Output

The program produces a graph comparing

- Monte Carlo simulation
- Analytical exponential decay

---

## Repository Contents

- `decay.py` — Python source code
- `decay.png` — Simulation result
- `Explanation.pdf` — Step-by-step explanation of the project
- `README.md`

---

## What I Learned

- Monte Carlo simulation of stochastic processes
- Boolean arrays in NumPy
- Random number generation
- Scientific plotting with Matplotlib
- Comparison between numerical simulation and analytical solutions
  
---

## Possible Future Improvements

- Variable decay constants
- Half-life calculation
- Multiple radioactive isotopes
- Radioactive decay chains
- Statistical analysis of repeated simulations

---

## Author

Shuvashish Sharma

Physics Undergraduate

Interested in Computational Physics, Nuclear Physics, and Scientific Computing.
