"""
Shopping Cart Program
Author: Cayden Champion
Date: 3/20/26
Purpose: Create a shopping cart program To help people with their shopping
"""
import math

items = []
prices = []

option = 0
# sum = 0

while option != 4:
    print("Please select one of the following:")
    print("1. Add Item")
    print("2. List items & total price")
    print("3. Remove Item")
    print("4. Quit")
    option = int(input("Which option do you want? "))
    if option == 1:
        item = input("\nWhat item would you like to add? ").capitalize()
        price = float(input(f"What is the price of {item}? $ "))
        print(f"{item} has been added to you cart.\n")
        items.append(item)
        prices.append(price)
    elif option == 2:
        total = sum(prices)
        print("\n#----Items----Prices")
        for i in range(len(items)):
            print(f"{i+1:<2} {items[i]:^8} ${prices[i]:>5.2f}")
        print(f"\nThe total price of these items is {total}")
        print()
    elif option == 3:
        if len(items) == 0:
            print("Your cart is empty.")
        else:
            remove_num = int(input("Which item number would you like to remove? "))
        
            if 1 <= remove_num <= len(items):
                print(f"\n{items[remove_num -1]} has been removed.\n")

                items.pop(remove_num - 1)
                prices.pop(remove_num - 1)
            else:
                print("That item number does not exist.")
    elif option == 4:
        print("See you later!")
    else:
        print("Invalid option. Please choose 1-4.")
