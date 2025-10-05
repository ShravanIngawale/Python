print("================= User Registration Form =================\n")

name = input("Enter your full name: ")
email = input("Enter your email address: ")
address = input("Enter your address: ")

formatted_name = name.title()
email = email.lower()
centered_address = address.center(45, "-")

print("\n================= Formatted User Data =================")
print("Name:", formatted_name)
print("Email:", email)
print("Address:", centered_address)

print("\nSome Checks:")
print("Is name all alphabets? ->", formatted_name.replace(" ", "").isalpha())
print("Does email end with '@gmail.com'? ->", email.endswith("@gmail.com"))
print("Address length count of spaces:", address.count(" "))