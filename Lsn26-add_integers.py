

# adds all of the integers from 1 up to 
# and including an integer that is entered by the user

int = int(input("Add integers from 1 up to including what integer? "))
sum = 0
for i in range(1, int + 1):
    sum += i
print(f"The sum of the integers from 1 up to and including {int} is {sum}.")