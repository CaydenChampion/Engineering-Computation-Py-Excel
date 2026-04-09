import math
import matplotlib.pyplot as plt
import numpy as np

# Plot a polynomial
# coef = [6,-8,4]
# x = np.linspace(-10,10,100)
# y = np.polyval(coef,x)
# plt.plot(x,y)
# plt.grid(True)
# plt.show()

# Find the roots of the polynomial
# my_roots = np.roots(coef)
# print(f"\nA polynomial with coefficients of {coef}")
# print(f"Has roots {my_roots}\n")

# Higher-order polynomial
coef = [6,8,2,0,9,-10]
my_roots = np.roots(coef)
print(f"\nA polynomial with coefficients of {coef}")
print(f"Has roots")
for i in range(len(my_roots)):
    print(f'{my_roots[i]:15.3f}')