# create and display items and prices

#display message to user
print ("\nEnter items and thier corresponding prices.")

#initialize lists
items = []
prices = []
item = 'initial value'

while item != 'End':
    item = input(f"\nWhat item do you want to add ('end' to quit)? ").capitalize()
    if item != 'End':
        price = float(input(f"What is the price of {item.lower()}? $"))
        items.append(item)
        prices.append(price)

print("\nItems       Prices")
for i in range(len(items)):
    print(f"{items[i]:<10} ${prices[i]:.2f}")


max_price = prices[0]
max_item = items[0]

for i in range(len(items)):
    if prices[i] > max_price:
        max_price = prices[i]
        max_item = items[i]

print(f'\nThe total price of your items is: ${sum(prices):.2f}')
print(f'{max_item} had the highest price of ${max_price:.2f}')