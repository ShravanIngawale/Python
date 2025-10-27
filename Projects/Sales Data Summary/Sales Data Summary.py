# Read the data from the file
sales = []
with open("Sales Data.csv", 'r') as f:
    lines = f.readlines()[1:] # skip header
    for line in lines:
        date, product, quantity, price = line.strip().split(',')
        sales.append({
            "date": date,
            "product": product,
            "quantity": int(quantity),
            "price": int(price)
        })

# Calculate total revenue
total_revenue = 0        
for s in sales:
    total_revenue += s["quantity"] * s["price"]

# Find best selling product
product_sales = {}    
for s in sales:
    if s["product"] in product_sales:
        product_sales[s["product"]] += s["quantity"]
    else:
        product_sales[s["product"]] = s["quantity"]

best_product = max(product_sales, key=product_sales.get)

# Find total and average sales per day
daily_sales = {}
for s in sales:
    revenue = s["quantity"] * s["price"]
    if s["date"] in daily_sales:
        daily_sales[s["date"]] += revenue
    else:
        daily_sales[s["date"]] = revenue

average_daily_sales = sum(daily_sales.values()) / len(daily_sales)

# Write summary report to a file
file = [
    "SALES SUMMARY REPORT\n"
    "====================\n"
    f"Total Revenue: ₹{total_revenue}\n",
    f"Average Daily Sales: ₹{average_daily_sales:.2f}\n"
    f"Best Selling Product: {best_product}\n\n"
    "Sales by Product:\n"
]
with open("Sales Summary.txt", 'w') as f:
    f.writelines(file)
    for product, qty in product_sales.items():
        f.write(f"- {product}: {qty} units\n")