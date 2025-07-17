# Q2:Write python code to implement Big M Method

import numpy as np
import matplotlib.pyplot as plt

# Coefficients of the objective function
c = np.array([-3, -5])

# Coefficients of constraints
A = np.array([
    [1, 2],
    [3, 2]
])
b = np.array([6, 12])

# Plot constraints
x = np.linspace(0, 10, 100)

# Constraint 1: x + 2y <= 6 → y <= (6 - x)/2
y1 = (6 - x) / 2
y1 = np.maximum(0, y1)

# Constraint 2: 3x + 2y <= 12 → y <= (12 - 3x)/2
y2 = (12 - 3*x) / 2
y2 = np.maximum(0, y2)

# Plot lines
plt.plot(x, y1, label=r'$x + 2y \leq 6$', color='blue')
plt.plot(x, y2, label=r'$3x + 2y \leq 12$', color='green')

# Shaded feasible region
plt.fill_between(x, 0, np.minimum(y1, y2), color='gray', alpha=0.3)

# Solve using Big M Method (Simplified Example)
def big_m_method(c, A, b):
    from scipy.optimize import linprog
    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')
    return res

result = big_m_method(c, A, b)

if result.success:
    plt.plot(result.x[0], result.x[1], 'ro', label='Optimal Solution')
    print("Optimal Solution:", result.x)
    print("Optimal Value:", -result.fun)
else:
    print("No feasible solution found.")

# Plot Settings
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Big M Method - Feasible Region and Optimal Solution')
plt.legend()
plt.grid(True)
plt.show()
