foods = []
prices = []
total = 0


def main():
    while True:
        food = input("\nEnter a food to buy (q to quit): ").strip().title()

        if food.lower() in ["q", "quit"]:
            break

        if not food or food.isdigit():
            print("Invalid food name. Try again.")
            continue

        while True:
            try:
                price = float(input(f"Enter the price of {food}: $"))
                if price <= 0:
                    print("Price must be a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid price. Enter a number.")

        foods.append(food)
        prices.append(price)


main()

if foods:
    print("\n----- YOUR CART -----")
    for food in foods:
        print(food, end=" ")

    for price in prices:
        total += price

    print(f"\nYour total is: ${total:.2f}\n")
else:
    print("No items were added.\n")
