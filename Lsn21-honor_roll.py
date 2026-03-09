GPA = float(input('What was your grade point average? '))
lowest_grade = float(input('What was your lowest grade? '))

print('US Scale')
if GPA >= 3.5 and lowest_grade >= 3.0:
    print('Congratulations! You made the honor roll!')
else:
    print('Sorry, you did not make the honor roll.')

print('\n')
print('Canadian Scale')
if GPA >= .85 and lowest_grade >= .70:
    print('Congratulations! You made the honor roll!')
else:
    print('Sorry, you did not make the honor roll.')