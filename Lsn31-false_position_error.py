import math

# Define the function
def f(x):
    return 2 * x**2 - 9 * math.sqrt(x)

# False Position Method with error tolerance
def false_position(xl, xu, err_tol):
    print()

    xrt = xl
    xrt_old = xl
    err = 100
    iter_count = 0

    while err > err_tol:
        xrt_old = xrt

        # False Position formula
        xrt = xl - f(xl) * (xu - xl) / (f(xu) - f(xl))

        # Calculate error EVERY iteration (including first)
        err = abs((xrt - xrt_old) / xrt) * 100

        iter_count += 1

        print(f"Iter: {iter_count:2d}   x-root: {xrt:.6f}   error: {err:.6f}")

        # Update bracket
        if f(xl) * f(xrt) < 0:
            xu = xrt
        else:
            xl = xrt

    return xrt, err, iter_count


# Initial values
x_lower = 2.5
x_upper = 3.0
error_tol = 0.01   # percent

# Check for valid bracket
if f(x_lower) * f(x_upper) > 0:
    print("\nYour interval does not bracket the root.\n")
else:
    root, error, iterations = false_position(x_lower, x_upper, error_tol)

    print(f"\nAfter {iterations} iteration the final estimate of the root is")
    print(f"{root:.6f} with a relative error of {error:.6f} %")
