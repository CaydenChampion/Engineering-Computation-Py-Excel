"""
Author: Cayden Champion
File: Integrator
Date: 4/3/26
"""
import numpy as np

def my_fun(x):
    return 2*x**3 + 4*x**2 + 5*x + 7

def true_integral(x):
    return (2*x**4)/4 + (4*x**3)/3 + (5*x**2)/2 + 7*x


print("\nThis program approximates the integral of the")
print("equation that is stored in the 'my_fun' function.\n")

low_limit = float(input("What is the lower limit of integration? "))
up_limit = float(input("What is the upper limit of integration? "))

if up_limit <= low_limit:
    print("\nThe upper limit must be greater than the lower limit!\n")
else:
    delta = float(input("What is the step size (or delta x) value? "))

    if delta >= (up_limit - low_limit):
        print("\nThe step size must be less than the range of integration!\n")
    else:
        x = np.arange(low_limit, up_limit + delta, delta)

        if x[-1] > up_limit:
            x[-1] = up_limit

        area_total = 0
        for i in range(len(x)-1):
            trap = (x[i+1] - x[i]) * (my_fun(x[i]) + my_fun(x[i+1])) / 2
            area_total += trap

        true_val = true_integral(up_limit) - true_integral(low_limit)

        # relative error
        error = abs((true_val - area_total) / true_val) * 100

        print(f"\nIntegrating the function in the 'my_fun' function")
        print(f"from {low_limit:.1f} to {up_limit:.1f} with a step size of {delta} gives the following results:\n")

        print(f"Approximate value of the integral: {area_total:.3f}")
        print(f"True value of the integral: {true_val:.3f}")
        print(f"True relative error: {error:.3f} %\n")