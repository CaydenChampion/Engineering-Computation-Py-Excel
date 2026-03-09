import math # imports the math module to use mathematical functions and constants

print(4+5, '(+)') # gives addition answer
print(4-5, '(-)') # gives subtraction answer
print(4*5, '(*)') # gives multiplication answer
print(4/5, '(/)') # gives decimal answer
print(4//5, '(//)') # gives whole number answer by droping decimal
print(4%5, '(%)') # gives remainder
print(4**5, '(**)') # gives 4 to the power of 5
print('\n') # gives a new line
print(math.pi, '(math.pi)') # gives the value of pi
print(math.sqrt(16), '(math.sqrt(16))') # gives the square root of 16
print('\n')
##--------------------------------------------------------------
# # ft/sec to MPH Conversion

# # Known information
# ft_in_miles = 5280 # feet
# min_in_hour = 60 # minutes
# sec_in_minute = 60 # seconds

# ft_per_sec = float(input("Enter speed in feet per second: "))
# print()
# miles_per_hour = float(ft_per_sec) / ft_in_miles*sec_in_minute*min_in_hour

# print (f'That speed is {miles_per_hour} miles per hour.')

# sum = 37.54298
# print(f'The sume is {sum}')
# print(f'The sume is {sum:.2f}') # rounds to 2 decimal places
# print(f'The sume is {sum:.3e}') # gives scientific notation with 3 decimal places
##--------------------------------------------------------------
# # PSI Conversion

# psi_in_kpa = 6.89476 # kPa
# psi = float(input("Enter pressure in PSI: "))
# kpa = psi * psi_in_kpa

# print(f'That pressure is {kpa} kPa.\n')
##--------------------------------------------------------------
# # Area of a Circle

# radius = float(input("Enter the radius of a circle: "))
# area = math.pi * radius**2

# print(f'The area of the circle is {area:.2f}.\n')
##--------------------------------------------------------------
# # Volume of a Cylinder

# radius = float(input("Enter the radius of a cylinder: "))
# Length = float(input("Enter the length of a cylinder: "))
# volume = math.pi * radius**2 * Length

# print(f'The volume of the cylinder is {volume:.3f}.\n')
##--------------------------------------------------------------
# # Calculates future value of a one time present investment

# present_value = float(input("Enter the present value of the one-time investment: "))
# annual_rate = float(input("Enter the annual interest rate (as a decimal): "))
# years = float(input("Enter the number of years: "))
# future_value = present_value * (1 + annual_rate)**years

# print(f'''{present_value} deposited now at {annual_rate} annual interest
# will be worth {future_value:.2f} in {years} years.\n''')
