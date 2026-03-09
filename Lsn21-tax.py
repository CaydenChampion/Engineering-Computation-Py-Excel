price = float(input("Enter the price of the item: "))

if price >= 1.00:
    tax = price * 0.07
    print(f"The tax on the item is ${tax:.2f}.")
else:
    tax = price 
    print("The item is tax exempt.")