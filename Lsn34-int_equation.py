# Implement the trapezoid method to 
# approximate the integral of an equation
import numpy as np

# Define a function that contains the equation
# that we want to find the integral of
def my_fun(x):
    return 2*x**3 + 4*x**2 + 5*x + 7

# Introduce the program to the user
print("\nThis program approximates the integral of the")
print("eqaution that is stored in the 'my_fun' function.\n")

# Set up variable values
low_limit = 0
up_limit = 4
delta = .3
x = np.arange(low_limit,up_limit+delta, delta)
if x[-1] > up_limit:
    x[-1] = up_limit
print(x)

# Approximate the integral using the trapezoidal method
area_total = 0
for i in range(len(x)-1):
    trap_area = (x[i+1] - x[i]) * (my_fun(x[i]) +my_fun(x[i+1]))/2
    area_total += trap_area

# Display the final aprox of the integral
print(f'The value of the integral is {area_total:.3f}')