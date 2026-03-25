import math

choice = input("Do you want to calculate an AREA or a VOLUME? ").lower()

if choice == "area":
    shape = input("Do you want to find the area of a TRIANGLE or CIRCLE? ").lower()

    if shape == "triangle":
        base = float(input("What is the base of the triangle? "))
        height = float(input("What is the height of the triangle? "))

        area = 0.5 * base * height
        print(f"The area of the triangle is {area:.2f} units squared.")

    elif shape == "circle":
        radius = float(input("What is the radius of the circle? "))

        area = math.pi * radius**2
        print(f"The area of the circle is {area:.2f} units squared.")

    else:
        print("Invalid shape option.")

elif choice == "volume":
    shape = input("Do you want to find the volume of a SPHERE or CYLINDER? ").lower()

    if shape == "sphere":
        radius = float(input("What is the radius of the sphere? "))

        volume = (4/3) * math.pi * radius**3
        print(f"The volume of the sphere is {volume:.2f} units cubed.")

    elif shape == "cylinder":
        radius = float(input("What is the radius of the cylinder? "))
        length = float(input("What is the length of the cylinder? "))

        volume = math.pi * radius**2 * length
        print(f"The volume of the cylinder is {volume:.2f} units cubed.")

    else:
        print("Invalid shape option.")

else:
    print("Invalid option. Please choose AREA or VOLUME.")