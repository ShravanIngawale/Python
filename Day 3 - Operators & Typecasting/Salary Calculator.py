# Basic data
monthly_salary = 50005 # base salary
bonus = 8000 # performance bonus
tax_percentage = 10 #10%
months = 12

# 1. Total yearly salary with bonus
yearly_salary = (monthly_salary + bonus) * months

# 2. Tax to be paid annually
tax_amount = yearly_salary * tax_percentage / 100

# 3. Net salary after tax
net_salary = yearly_salary - tax_amount

# 4. Average monthly salary after tax
average_monthly_salary = net_salary // months

# 5. Remaining rupees that didn't divide equally per month
leftover_amount = net_salary % months

# 6. Future salary prediction (assuming 5% hike each year for 2 years)
future_salary = monthly_salary * (1.05 ** 2)

print("Yearly Salary with Bonus:", yearly_salary)
print("Tax Amount:", tax_amount)
print("Net Yearly Salary:", net_salary)
print("Average Monthly Salary (after tax):", average_monthly_salary)
print("Leftover Amount (after monthly split):", leftover_amount)
print("Predicted Monthly Salary after 2 Years (5% hike/year):",  round(future_salary, 2)) # Show only 2 decimal places