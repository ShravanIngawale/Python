name = input("Enter employee name: ")
department = input("Enter department: ")
role = input("Enter job title: ")
age = input("Enter age: ")
experience = input("Enter years of experience: ")
location = input("Enter office location: ")
contact = input("Enter contact number: ")
email = input("Enter official email address: ")
joining_year = input("Enter year of joining: ")

intro = "This is " + name + ". He/She works in the " + department + " department as a " + role + ". "
intro += "Currently " + age + " years old, with " + experience + " years of experience. "
intro += "Working at our " + location + " branch since " + joining_year + ". "
intro += "You can contact " + name + " at " + contact + " or via email at " + email + ". "
intro += name + " is known for being a dedicated and responsible member of the team."

print("\nEmployee Introduction:\n")
print(intro)