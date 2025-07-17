# Q2:Write python code to implement Somplex Method
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the coefficients of the objective function
# Example: Maximize z = 3x + 5y
# Since linprog does minimization, we multiply by -1 for maximization
c = [-3, -5]

# Define the inequality constraints (Ax <= b)
# Example Constraints:
# 1) x + 2y <= 6
# 2) 3x + 2y <= 12
# 3) x >= 0 (implied)
# 4) y >= 0 (implied)
A = [
    [1, 2],
    [3, 2]
]
b = [6, 12]

# Bounds for x and y
x_bounds = (0, None)  # x >= 0
y_bounds = (0, None)  # y >= 0

# Solving the Linear Programming Problem
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='simplex')

# Output the results
print("Optimal value (Maximized z):", -res.fun)
print("Optimal solution (x, y):", res.x)

# ---------------- Plotting Feasible Region ----------------

# Create a grid of x values
x = np.linspace(0, 10, 400)

# Define constraints as functions of x
y1 = (6 - x) / 2
y2 = (12 - 3*x) / 2

# Make the plot
plt.figure(figsize=(8, 6))

# Fill feasible region
y1_clip = np.clip(y1, 0, 10)
y2_clip = np.clip(y2, 0, 10)

plt.plot(x, y1, label=r'$x + 2y \leq 6$')
plt.plot(x, y2, label=r'$3x + 2y \leq 12$')
plt.xlim(0, 5)
plt.ylim(0, 5)

# Fill feasible region
plt.fill_between(x, 0, np.minimum(y1_clip, y2_clip), where=(y1_clip > 0) & (y2_clip > 0), color='lightgrey')

# Plot the optimal point
plt.plot(res.x[0], res.x[1], 'ro', label="Optimal Solution")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Feasible Region and Optimal Solution')
plt.legend()
plt.grid(True)
plt.show()
