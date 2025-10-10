total = 0

while True:
    price = int(input("Enter item price (0 to stop): "))

    if price == 0:
        print("Billing stopped")
        break

    total = total + price
    print("Added to bill. Current total =", total)

print("Final Bill Amount =", total)