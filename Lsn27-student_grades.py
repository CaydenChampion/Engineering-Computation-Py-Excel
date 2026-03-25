names = []
grades = []

print("Enter student names and their grades.")

while True:
    student = input("Enter student name ('end' to quit): ").capitalize()
    
    if student.lower() == "end":
        break
    
    grade = float(input(f"Enter grade for {student}: "))
    names.append(student)
    grades.append(grade)

print("\nStudent        Grade")
print("------------------------")
for i in range(len(names)):
    print(f"{names[i]:<15}{grades[i]:>7.2f}")

average = sum(grades) / len(grades)

max_grade = max(grades)
min_grade = min(grades)

max_index = grades.index(max_grade)
min_index = grades.index(min_grade)

print("\nStatistics:")
print(f"Average grade: {average:.1f}")
print(f"Highest grade: {max_grade:.2f} ({names[max_index]})")
print(f"Lowest grade: {min_grade:.2f} ({names[min_index]})")