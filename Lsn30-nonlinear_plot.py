import numpy as np
import matplotlib.pyplot as plt

# Given data points from Excel
v_data = np.array([0, 3, 8, 12, 15, 20, 23])
F_data = np.array([0, 0.03, 0.12, 0.35, 0.7, 1.25, 1.3])

# Constants from Excel
rho = 1.23     # kg/m^3
A = 0.01       # m^2
Cd = 0.47

# Create smooth velocity values for equation curve
v = np.linspace(0, 23, 100)

# Drag force equation
F = 0.5 * rho * A * Cd * v**2

# Plot
plt.figure()
# plt.xticks([0,5,10,15,20,25])
# plt.yticks([0,.2,.4,.6,.8,1,1.2,1.4,1.6,1.8])

# Plot equation (red line)
plt.plot(v, F, color = 'red', label = 'Equation')

# Plot data points (blue dots)
plt.scatter(v_data, F_data, color = 'blue', label = 'Data Points')

# Labels and title
plt.title('Drag Force Example')
plt.xlabel('v (m/s)')
plt.ylabel('F_drag (N)')

# Graph sizing
plt.xticks([0,5,10,15,20,25])
plt.yticks([0,.2,.4,.6,.8,1,1.2,1.4,1.6,1.8])

plt.grid()
plt.legend(loc = 'lower right')

plt.show()