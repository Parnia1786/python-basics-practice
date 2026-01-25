# A simple shopping cart program
# A simple Python program that lists user-defined foods with their prices and shows the total of the prices.

foods = []
prices = []
total = 0

print()

while True:
    food = input("Enter a food to buy (q to quit): ").lower().strip()
    if food in ["q", "quit"]:
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)


print()
print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total:.2}")
print()
