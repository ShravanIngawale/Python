# User's input (from an online shopping cart)
item_price = 299.99 # float
quantity = 2 # int
discount_percent = "10" # string

'''Implicit Typecasting
Python automatically convert int to float during calculation'''
total_cost = item_price * quantity # quantity is int, item_price is float
print("Total (before discount):",total_cost)
# Here, quantity (int) is implicitly converted to float

'''Explicit Typecasting 
Converting string discount to float before using it'''
discount_percent = float(discount_percent) # now it's 10.0

#Calculating discount
discount_amount = total_cost * (discount_percent / 100)

#Final bill
final_amount = total_cost - discount_amount

print("Discount Applied:", round(discount_amount, 2))
print("Final Amount to Pay:", round(final_amount, 2))