import math

# Given x and y components of a force
# find the resultant forca and angle

fx = float(input("Enter the x component of the force (in lbs): "))
fy = float(input("Enter the y component of the force (in lbs): "))
force = math.sqrt(fx**2 + fy**2)

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
else:
    angle = 180


print()
print(f'The magnitude of the resultant force is: {force:.1f} lbs.')
print(f'The angle of the resultant force is: {angle:.1f} degrees.')