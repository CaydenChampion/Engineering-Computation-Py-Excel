import math

# Multiplies all of the integers from 1 up to and 
# including an integer that is entered by the user.

int = int(input("What integer do you want to find the factorial of? "))

print("\nUsing a for loop:")
factorial = 1
for i in range(1, int + 1):
    factorial *= i
print(f"The factorial of {int} is {factorial}.")

print("\nUsing the built-in function fromt the math library:")
print(f"The factorial of {int} is {math.factorial(int)}.")