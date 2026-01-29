print("Hello, this is a simple caculator that you can use for free.")

def qu():
    a = input("Enter your equation: ").strip().replace(" ","")
    if "+" in a:
        a = a.split("+")
        a1 = float(a[0])
        a2 = float(a[1])
        print(round(a1+a2, 3))
    elif "-" in a:
        a = a.split("-")
        a1 = float(a[0])
        a2 = float(a[1])
        print(round(a1-a2, 3))
    elif "**" in a:
        a = a.split("**")
        a1 = float(a[0])
        a2 = int(a[1])
        print(round(a1**a2, 3))
    elif "*" in a:
        a = a.split("*")
        a1 = float(a[0])
        a2 = float(a[1])
        print(round(a1*a2, 3))
    elif "/" in a:
        a = a.split("/")
        a1 = float(a[0])
        a2 = float(a[1])
        print(round(a1/a2, 3))
    else:
        print("Invalid input. Please try again.")

qu()
