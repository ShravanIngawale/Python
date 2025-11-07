purchases = []

with open("purchases.csv", 'r') as f:
    lines = f.readlines()[1:]
    for line in lines:
        customer, product, quantity, price = line.strip().split(",")
        purchases.append({
            "customer": customer,
            "product": product,
            "quantity": int(quantity),
            "price": float(price)
        })

customer_spending = {}
for p in purchases:
    total = p["quantity"] * p["price"]
    if p["customer"] in customer_spending:
        customer_spending[p["customer"]] += total
    else:
        customer_spending[p["customer"]] = total

best_customer = max(customer_spending, key=customer_spending.get)
total_sales = sum(customer_spending.values())

with open("Customer Purchase Report.txt", 'w') as f:
    file = [
        "CUSTOMER PURCHASE REPORT\n"
        "========================\n"
        f"Total Sales: ₹{total_sales:.2f}\n"
        f"Top Customer: {best_customer} (₹{customer_spending[best_customer]:.2f})\n\n"
        "Spending by Customer:\n"
    ]
    f.writelines(file)
    for customer, total in customer_spending.items():
        f.write(f"- {customer}: ₹{total:.2f}\n")

print("Report generated successfully! File saved as 'Customer Purchase Report.txt'")