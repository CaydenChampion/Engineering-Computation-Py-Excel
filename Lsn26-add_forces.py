import math

num_forces = int(input("How many forces do you want to enter? "))
forces = []
angles = []
fx = 0   #Running totals for x components
fy = 0   #Running totals for y components

for i in range(num_forces):
    magnitude = float(input(f"\nWhat is the magnitude of force #{i+1} (in lbs)? "))
    angle = float(input(f"What is the angle (in degrees) of force #{i+1}? "))
    forces.append(magnitude)
    angles.append(angle)
    # Convert angle to radians for calculation
    # Calculate x and y components
    fx = fx + magnitude * math.cos(math.radians(angle))
    fy = fy + magnitude * math.sin(math.radians(angle))
    
force = math.sqrt(fx**2 + fy**2)

print(f'The magnitude of the resultant force is {force:.2f} lbs.\n')