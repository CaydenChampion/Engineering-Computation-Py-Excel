# Write a program that asks the user to enter student 
# names and their corresponding grades. 

num_students = int(input("How many students do you need to enter grades for? "))
students = {}

for i in range(num_students):
    name = input(f"Name of student #{i + 1}: ").capitalize()
    grade = float(input(f"Enter {name}'s grade: "))
    students[name] = grade

print("\nStudent Grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")

ave = sum(students.values()) / len(students)
highest_grade = max(students.values())
lowest_grade = min(students.values())

print(f"\nThe average grade: {ave:.1f}")
print(f'{list(students.keys())[list(students.values()).index(highest_grade)]} has the highest grade: {highest_grade:.0f}')
print(f'{list(students.keys())[list(students.values()).index(lowest_grade)]} has the lowest grade: {lowest_grade:.0f}')