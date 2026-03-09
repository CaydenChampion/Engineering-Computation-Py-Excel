import math
print()
# Scenario 1
A = 75  # angle A in degrees
a = 2 # side a in inches
b = a/math.tan(math.radians(A)) 
print (f'For scenario 1, the length of side b is: {b:.3f} inches.')

# Scenario 2
a = 3  # side a in inches
c = 5  # side c in inches
B = math.degrees(math.acos(a/c))
print (f'For scenario 2, the measure of angle B is: {B:.3f} degrees.')

# Scenario 3
a = 1 # side a in inches
c = 4 # side c in inches
A = math.degrees(math.asin(a/c))
print (f'For scenario 3, the measure of angle A is: {A:.3f} degrees.')

# Scenario 4
a = 2 # side a in inches
b = 4 # side b in inches
B = math.degrees(math.atan(b/a))
c = math.sqrt(a**2 + b**2)
print (f'For scenario 4, the measure of angle B is: {B:.3f} degrees.')
print (f'For scenario 4, the length c is: {c:.3f} inches.')