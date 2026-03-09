import math

print()
print('''This program will add two forces together 
and display the resultant force and angle.''')

force1 = float(input("Enter the magnitude of the first force (in lbs): "))
angle1 = float(input("Enter the angle of the first force (in degrees): "))
force2 = float(input("Enter the magnitude of the second force (in lbs): "))
angle2 = float(input("Enter the angle of the second force (in degrees): "))

# Calculate the x and y components of the first force
fx1 = force1 * math.cos(math.radians(angle1))
fy1 = force1 * math.sin(math.radians(angle1))
# Calculate the x and y components of the second force
fx2 = force2 * math.cos(math.radians(angle2))
fy2 = force2 * math.sin(math.radians(angle2))
# Add the x and y components of the two forces
fx = fx1 + fx2
fy = fy1 + fy2
# Calculate the magnitude of the resultant force
force = math.sqrt(fx**2 + fy**2)
# Calculate the angle of the resultant force
if fx > 0 and fy > 0:
    angle = math.degrees(math.atan(fy/fx))
elif fx < 0 and fy > 0:
    angle = math.degrees(math.atan(fy/fx)) + 180
elif fx < 0 and fy < 0:
    angle = math.degrees(math.atan(fy/fx)) + 180
elif fx > 0 and fy < 0:
    angle = math.degrees(math.atan(fy/fx)) + 360
elif fx == 0 and fy > 0:
    angle = 90
elif fx == 0 and fy < 0:
    angle = 270
elif fx > 0 and fy == 0:
    angle = 0
elif fx < 0 and fy == 0:
    angle = 180
else:
    angle = 180

print()
print(f'The magnitude of the resultant force is: {force:.1f} lbs.')
print(f'The angle of the resultant force is: {angle:.1f} degrees.')