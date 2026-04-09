import numpy as np

# DEFINE MATRICES, uncomment the ones you need

# 2 x 2
A = np.array([[1, -6],
              [4, 12]])
b = np.array([5, 7])

# 3 x 3
# A = np.array([[1, 0, 7],
#               [2, -4, 3],
#               [5, 6, 0]])
# b = np.array([2, 7, 4])

# 4 x 4
# A = np.array([[0,0,0,0],
#               [0,0,0,0],
#               [0,0,0,0],
#               [0,0,0,0]])
# b = np.array([0,0,0,0])

# 5 x 5
# A = np.array([[0,0,0,0,0],
#               [0,0,0,0,0],
#               [0,0,0,0,0],
#               [0,0,0,0,0],
#               [0,0,0,0,0]])
# b = np.array([0,0,0,0,0])


if np.linalg.det(A) == 0:
    print("\nThe A matrix is singular so")
    print("the system cannot be solved!\n")
else:
    x = np.linalg.solve(A, b)

    # Display results
    print("\nA Matrix:")
    print(A)

    print("\nb Vector:")
    print(b)

    print("\nx Values:")
    for i in range(len(x)):
        print(f"x{i+1} = {x[i]:.3f}")

    print("\nFull x array:")
    print(x)