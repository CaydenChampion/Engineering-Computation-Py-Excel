import math
# Given a force and an angle, find the
# x and y components of the force

print()

force = float(input("Enter the magnitude of the force (in lbs): "))
angle = float(input("Enter the angle of the force (in degrees): "))

# Calculate the x and y components of the force
fx = force * math.cos(math.radians(angle))
fy = force * math.sin(math.radians(angle))

print()
print(f'The x component of the force is: {fx:.1f} lbs.')
print(f'The y component of the force is: {fy:.1f} lbs.')

