# Approximate the integral of an equation 
# using the trapezoidal rule

# Store the equation in a python function
def my_fun(x):
    value_of_equation = -2*x**2 + 10*x + 18
    return value_of_equation

# Itegrate the equation from 0 to 5

# Single trapezoid
trap_area = (4-0)*(my_fun(0)+my_fun(4))/2
print(f"\nUsing 1 trapeziod, the integral is approximatley {trap_area:.1f}")

# Two trapezoids
trap1_area = (2-0)*(my_fun(0)+my_fun(2))/2
trap2_area = (4-2)*(my_fun(2)+my_fun(4))/2
total_area = trap1_area + trap2_area
print(f"Using 2 trapeziod, the integral is approximatley {total_area:.1f}\n")