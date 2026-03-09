country = input("Enter the country you are in: ")
province = input("Enter the province you are in: ")

if country.lower == "canada":
    if province.lower == "alberta":
        tax = 0.05
        print(f"The tax rate in {province} is {tax:.2%}.")
    elif province.lower == "nunavat":
        tax = 0.05
        print(f"The tax rate in {province} is {tax:.2%}.")
    elif province.lower == "Yukon":
        tax = 0.05
        print(f"The tax rate in {province} is {tax:.2%}.")
    elif province.lower == "ontario":
        tax = 0.13
        print(f"The tax rate in {province} is {tax:.2%}.")

        # Any povince not listed above is 15% (or .15)tax
else:
    tax = 0.15
    print(f"The tax rate in {province} is {tax:.2%}.")