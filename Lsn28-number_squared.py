# # Function that performs a task
# def print_message():
#     print ('\nYou just call the print_message function')

# print_message()


#function that recieves an input value and perfoms
# a task on that input value
# def square_number(number):
#     number_squared = number**2
#     print (f'The value of {number} squared is {number_squared}\n')

# square_number(3)

# Function that recieves an input value and perfoms
# a task on that input value, and returns an ouput value
def square_number(number):
    number_squared = number**2
    return number_squared

# result = square_number(3)
# print(result)
print(f'\nThe result is {square_number(3)}.\n')