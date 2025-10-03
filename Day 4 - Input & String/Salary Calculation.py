monthly_salary = float(input("Enter monthly salary: "))
bonus = float(input("enter yearly bonus: "))
tax_percentage = float(input("Enter tax percentage: "))
months =12

yearly_salary = (monthly_salary + bonus) * months
tax_amount = yearly_salary * tax_percentage / 100
net_salary = yearly_salary - tax_amount
average_monthly_salary = net_salary // months
leftover_amount = net_salary % months
future_salary = monthly_salary * (1.05 ** 2)

print("\nYearly Salary with Bonus:", yearly_salary)
print("Tax Amount:", tax_amount)
print("Net Yearly Salary:", net_salary)
print("Average Monthly Salary:", average_monthly_salary)
print("Leftover Amount:", leftover_amount)
print("Predicted Monthly Salary after 2 Years:", round(future_salary, 2))