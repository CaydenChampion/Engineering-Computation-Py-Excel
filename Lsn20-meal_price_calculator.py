"""
Class: Engineering Computation
Title: Meal Price Calculator
Author: Cayden Champion
Date: 02/27/2026
"""

print('This program will calculate the total cost of a meal')

child = float(input("What is the price of a chil'd meal (in $)? "))
adult = float(input("What is the price of an adult meal (in $)? "))
num_child = int(input("How many children are there? "))
num_adult = int(input("How many adults are there? "))
tax_rate = float(input("What is the tax rate (enter 0.05 for 5%)? "))

#calculations
subtotal = child * num_child + adult * num_adult

print(f'''Suggested tip amounts:
      15% = ${subtotal * 0.15:.2f}
      18% = ${subtotal * 0.18:.2f}
      20% = ${subtotal * 0.20:.2f}''')
tip = float(input("Please enter tip amount (in dollars): "))

#payment amount
print(f'\nSubtotal: ${subtotal:.2f}')
print(f'Sales tax: ${subtotal * tax_rate:.2f}')
print(f'Tip: ${tip:.2f}')
print('-----------------------------')
print(f'Total: ${subtotal + subtotal * tax_rate + tip:.2f}\n\n')

payment_amount = float(input("Enter the payment amount: "))
change = payment_amount - (subtotal + subtotal * tax_rate + tip)
print(f'Change: ${change:.2f}\n')

print('Thank you for dining with us!')