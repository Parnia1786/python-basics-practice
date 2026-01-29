print("Hello, this is a simple calculator that you can use for free.")

def qu():
    a = input("Enter your equation: ").strip().replace(" ", "")
    if "**" in a:
        a = a.split("**")
        a1 = float(a[0])
        a2 = int(a[1])
        print(round(a1 ** a2, 3))
    elif "+" in a:
        a = a.split("+")
        a1 = float(a[0])
        a2 = float(a[1])
        print(round(a1 + a2, 3))
    elif "%" in a:
        a = a.split("%")
        a1 = float(a[0])
        a2 = float(a[1])
        print(round(a1 % a2, 3))
    elif "-" in a:
        a = a.split("-")
        a1 = float(a[0])
        a2 = float(a[1])
        print(round(a1 - a2, 3))
    elif "*" in a:
        a = a.split("*")
        a1 = float(a[0])
        a2 = float(a[1])
        print(round(a1 * a2, 3))
    elif "/" in a:
        a = a.split("/")
        a1 = float(a[0])
        a2 = float(a[1])
        print(round(a1 / a2, 3))
    else:
        print("Invalid input. Please try again.")

def ab():
    while True:
        qu()
        c = input("Do you want to continue? (yes/no): ").lower().strip()
        if c == 'yes' or c == 'y':
            print("\nOk! Give me a new equation...")
            continue
        elif c == 'no' or c == 'n':
            print("\nGoodbye! Have a nice day.")
            break
        else:
            print("Invalid input. Please type yes or no.")
ab()
