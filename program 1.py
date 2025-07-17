#Q1:Solve the following LLP by Python
# OBJ func: Lp= 3x+5y
# constraint: 2x+3y>=12 , -x+y<=3 , x>=4 , y<=3.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define coefficients for the objective function
c = [-3, -5]  # Maximization -> Convert to Minimization by negating

# Define inequality constraints in the form Ax <= b
A = [[-2, -3],  # 2x + 3y >= 12  -> -2x - 3y <= -12
     [1, -1],   # -x + y <= 3  -> x - y <= 3
     [-1, 0],   # x >= 4  -> -x <= -4
     [0, 1]]    # y <= 3  -> y <= 3

b = [-12, 3, -4, 3]

# Solve the linear programming problem
res = linprog(c, A_ub=A, b_ub=b, method='highs')

# Print optimal solution
if res.success:
    print("Optimal Solution (x, y):", res.x)
    print("Maximum Value of Z:", -res.fun)  # Convert back to maximization
else:
    print("No optimal solution found.")

# Plotting the feasible region
x_vals = np.linspace(0, 10, 100)
y_vals1 = (12 - 2*x_vals) / 3  # 2x + 3y = 12
y_vals2 = x_vals - 3  # -x + y = 3
y_vals3 = np.full_like(x_vals, 3)  # y = 3
x_bound = np.full_like(x_vals, 4)  # x = 4

# Plot constraints
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals1, label=r'$2x + 3y \geq 12$', color='blue')
plt.plot(x_vals, y_vals2, label=r'$-x + y \leq 3$', color='green')
plt.axhline(y=3, color='purple', linestyle='--', label=r'$y \leq 3$')
plt.axvline(x=4, color='red', linestyle='--', label=r'$x \geq 4$')

# Fill feasible region
y_min = np.maximum(y_vals1, -np.inf)
y_max = np.minimum(y_vals2, 3)
plt.fill_between(x_vals, y_min, y_max, where=(x_vals >= 4), color='gray', alpha=0.3)

# Mark optimal solution
if res.success:
    plt.scatter(res.x[0], res.x[1], color='red', zorder=5, label='Optimal Solution')
    plt.text(res.x[0], res.x[1], f'({res.x[0]:.2f}, {res.x[1]:.2f})', fontsize=12, verticalalignment='bottom')

# Labels and legend
plt.xlim(0, 10)
plt.ylim(0, 6)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Feasible Region and Optimal Solution')
plt.grid()
plt.show()



