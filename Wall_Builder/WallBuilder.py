# Wall Builder: prints a rectangular wall of given size and symbol

while True:
    try:
        while True:
            rows = int(input("Enter the number of rows: "))
            if rows==0:
                print("Invalid input. Rows must not be zero. Try again.")
                rows = int(input("Enter the number of rows: "))
            else:
                break
            
        while True:
            columns = int(input("Enter the number of columns: "))
            if columns==0:
                print("Invalid input. Columns must not be zero. Try again.")
                columns = int(input("Enter the number of columns: "))
            else:
                break
            
        symbol = input("Enter the symbol: ")
        break

    except ValueError:
        print("Invalid input. Rows and columns must be integers. Try again.")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
