"""
File: Linear equations tool
Author: Cayden Champion
Date:3/27/26
"""
import numpy as np

# Display message to user
print('\nWelcome to the Linera Equations Tool!')

# Get input from user
num_eq = int(input("How many equations and how many unkowns are there? "))

# Initialize matrices
A = np.zeros((num_eq,num_eq))
b = np.zeros(num_eq)

#build the A Matrix
for row in range(num_eq):
    print(f"\n[A] matrix values for row {row+1}")
    for column in range(num_eq):
        A[row, column] = float(input(f"Column {column+1}: "))
print()

# Check to see if the A matrix is singular
if np.linalg.det(A) == 0:
    print("The A matrix is singular so")
    print("the system cannot be solved!")
else:
    # Build the b vector
    for row in range(num_eq):
        b[row] = float(input(f"[b] vector values for row {row+1}: "))
    print()

    # Solve system
    x = np.linalg.solve(A, b)

    # Display results
    print("A Matrix: \n{A}")
    print("\nb Vector: \n{b}")
    print("\nx Values:")
    for i in range(num_eq):
        print(f"x{i+1} = {x[i]:.3f}")









# a = np.zeros(5)
# print(a)

# b = np.ones((2,3))
# print(b)

# a[3] = 5
# print(a)

# print(a[0])
# print(a[3])

# b[0,1] = 15
# print(b)

# print(b[1,1])
# print(b[0,1])

# x = np.array([1,2,3,4,5])
# print(x[2])

# x[2] =10
# print(x)

# y = np.array([[1,2,3],[4,5,6]])
# print(y[1,2])

# y[1,2] = 25
# print(y)

