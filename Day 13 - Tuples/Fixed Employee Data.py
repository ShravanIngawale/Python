employee = (
    (101, "Rahul Sharma", "Sales"),
    (102, "Priya Singh", "HR"),
    (103, "Amit Kumar", "IT")
)

print("All Employee:", employee)

second_employee_department = employee[1] [2]
print("\nSecond employee's department:", second_employee_department)

emp_id, emp_name, emp_dept = employee[0]
print("\nFirst Employee Info:")
print("ID:", emp_id)
print("Name:", emp_name)
print("Department:", emp_dept)