foods = []
prices = []
total = 0

print()

def main():
    while True:
        food = input("\nEnter a food to buy (q to quit): ").title().strip()
        
        if food in ["Q", "Quit"]:
            break
        elif food in ["", " "]:
            print("Invalid input. Try again. ")
            continue
        else:
            while True:
                try:
                    price = float(input(f"\nEnter the price of a {food}: $"))
                    if price in ["", " ", 0] or price < 0:
                        print("Invalid input. Must be float and positive. Try again.")
                    else:
                        foods.append(food)
                        prices.append(price)
                        break
                except ValueError:
                    print("Invalid input. Must be flaot. Try again.")
                    continue
    


while True:
    main()
    if foods==[]:
        print("You should input the food's name. ")
        pass_program = input("If you want to pass the program write 'pass'.\nBut if you don't want to pass the program, write anything else: ").strip().lower()
        if not pass_program=='pass':
            main()
        elif pass_program=='pass':
            quit = input("\nAre you sure (yes or no)? ").strip().lower()
            if quit in ["y", "yes"]:
                print("Have a nice day. Goodbye! \n")
                break
            elif quit in ["n", "no"]:
                main()
            else:
                print("Invalid input. Try again later. Goodbye. ")

    else:
        break


if not foods==[]:
    print()
    print("----- YOUR CART -----")

    for food in foods:
        print(food, end=" ")
    for price in prices:
        total += price

    print()
    print(f"Your total is: ${total:.2}")
    print()
