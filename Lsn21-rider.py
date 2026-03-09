# Determine if a rider is allowed to ride a roller coaster based on height and age.
height = float(input("Enter the rider's height in inches: "))
age = int(input("Enter the rider's age: "))
riders = input("Enter the number of riders (single or multiple): ")

if height >= 38 and age >= 18 or riders.lower() == "multiple":
    can_ride = True
else:
    can_ride = False

if can_ride:
    print("The rider is allowed to ride the roller coaster.")
else:
    print("The rider is not allowed to ride the roller coaster.")
