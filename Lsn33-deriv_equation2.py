import numpy as np
import matplotlib.pyplot as plt

# Define the function
def fun(x):
    return 4*x**2 - 12*x + np.exp(0.5*x)

# Define the TRUE derivative
def true_deriv(x):
    return 8*x - 12 + 0.5*np.exp(0.5*x)

# Divided difference methods
def forward(xi, xi_plus):
    return (fun(xi_plus) - fun(xi)) / (xi_plus - xi)

def backward(xi, xi_minus):
    return (fun(xi) - fun(xi_minus)) / (xi - xi_minus)

def centered(xi_plus, xi_minus):
    return (fun(xi_plus) - fun(xi_minus)) / (xi_plus - xi_minus)

# Create x values
x = np.arange(0, 5.1, 0.1)
y = fun(x)

# Approximate derivative
deriv = []
for i in range(len(x)):
    if i == 0:
        deriv.append(forward(x[i], x[i+1]))
    elif i == len(x)-1:
        deriv.append(backward(x[i], x[i-1]))
    else:
        deriv.append(centered(x[i+1], x[i-1]))

# True derivative values
true_vals = true_deriv(x)

# Print results
print("\n x     f(x)     approx f'(x)     true f'(x)")
for i in range(len(x)):
    print(f"{x[i]:3.1f} {y[i]:10.3f} {deriv[i]:12.2f} {true_vals[i]:12.2f}")

# Plot
plt.plot(x, y, label='f(x)')
plt.plot(x, deriv, label="Approx Derivative")
plt.plot(x, true_vals, '--', label="True Derivative")

plt.grid(True)
plt.legend(loc="best")
plt.xlabel("x")
plt.title("Function and Derivatives")
plt.show()