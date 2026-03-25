"""
Author: Cayden
Date: 2024-06-17
This program allows the user to perform various force calculations, 
including breaking a force into its components, combining components into a resultant force,
and adding multiple forces together.
"""
import math

print ('You may do the following:')
print ('1. Break a force into its x and y components.')
print ('2. Combine component forces into resultant force and angle.')
print ('3. Add multiple forces.')
choice = int(input('Which option do you want? '))

if choice == 1:
    magnitude = float(input('What is the magnitude of the force (in lbs)? '))
    angle = float(input('What is the angle (in degrees) of the force? '))
    fx = magnitude * math.cos(math.radians(angle))
    fy = magnitude * math.sin(math.radians(angle))
    print(f'The x component of the force is {fx:.1f} lbs.')
    print(f'The y component of the force is {fy:.1f} lbs.\n')
elif choice == 2:
    fx = float(input('What is the x component of the force (in lbs)? '))
    fy = float(input('What is the y component of the force (in lbs)? '))
    magnitude = math.sqrt(fx**2 + fy**2)
    angle = math.degrees(math.atan(fy/fx))

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

    print(f'The magnitude of the force is {magnitude:.1f} lbs.')
    print(f'The angle of the force is {angle:.1f} degrees.\n')

elif choice == 3:
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

    print("\n#    Force (lbs)   Angle (deg)")
    for i in range(len(forces)):
        print(f"{i+1:<2} {forces[i]:^10} {angles[i]:>10.1f}")

    print()
    print(f'The magnitude of the resultant force is {force:.1f} lbs.')
    print(f'The angle of the resultant force is {math.degrees(math.atan2(fy, fx)):.1f} degrees.\n')
else:
    print('That is not a valid choice.\n')
