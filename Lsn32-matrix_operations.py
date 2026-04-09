import numpy as np

# Define Matrices
A = np.array([[5, 2],[4, -3]])
C = np.array([[1, 2],[2, 3]])
b = np.array([8,1])

# Matrix operations
A_times_C = np.dot(A,C)
A_determ = np.linalg.det(A)
A_inv = np.linalg.inv(A)
A_times_A_inv = np.dot(A,A_inv)
A_inv_times_b = np.dot(A_inv,b)
solution2 = np.linalg.solve(A,b)

# Print results
print(f'\nA Matrix\n{A}')
print(f'\nC Matrix\n{C}')
print(f'\nA x C Matrix\n{A_times_C}')
print(f'\nDeterminant of A\n{A_determ}')
print(f'\nInverse of A\n{A_inv}')
print(f'\nA_inv x b\n{A_inv_times_b}')
print(f'\nSolution 2\n{solution2}')