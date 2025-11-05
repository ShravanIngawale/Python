with open("Expenses.csv", 'w') as f:
    f.write("Date,Category,Amount\n")

def add_expense():
    date = input("Enter date (YYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc.): ")
    amount = input("Enter amount: ")

    with open("Expenses.csv", 'a') as f:
        f.write(f"{date},{category},{amount}\n")

    print("Expense added successfully!\n")

def view_expenses():
    print("\n--- ALL EXPENSES ---")
    with open("Expenses.csv", 'r') as f:
        lines = f.readlines()[1:]
        if not lines:
            print("No expense found.\n")
            return
        for line in lines:
            date, category, amount = line.strip().split(",")
            print(f"{date} | {category} | ₹{amount}")
    print()

def show_summary():
    total_expense = 0
    category_expense = {}

    with open("Expenses.csv", 'r') as f:
        lines = f.readlines()[1:]
        for line in lines:
            date, category, amount = line.strip().split(",")
            amount = float(amount)
            total_expense += amount

            if category in category_expense:
                category_expense[category] += amount
            else:
                category_expense[category] = amount

    print("\n--- EXPENSE SUMMARY ---")
    print(f"Total Expenses: ₹{total_expense:.2f}")
    print("Spending by Category:")
    for cat, amt in category_expense.items():
        print(f"- {cat}: ₹{amt:.2f}")
    print()

# Main menu loop
while True:
    print("=== EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Summary")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        show_summary()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")