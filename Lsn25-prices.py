# create and display items and prices

num_items = int(input("How many items do you need to enter prices for? "))

#initialize lists
items = []
prices = []

for i in range(num_items):
    new_item = input(f'\nWhat is item #{i+1}? ').capitalize()
    new_price = float(input(f'What is the price of {new_item.lower()}? $'))
    items.append(new_item)
    prices.append(new_price)

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