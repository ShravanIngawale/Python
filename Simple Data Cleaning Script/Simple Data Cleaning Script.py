cleaned_data =[]

with open("raw data.csv", 'r') as f:
    lines = f.readlines()[1:]

    for line in lines:
        # split and clean fields
        name, age, email = [value.strip() for value in line.strip().split(",")]

        # fill missing values
        if name == "":
            name = "Unknown"
        if age == "":
            age = "0"
        if email == "":
            email = "unknown@email.com"

        email = email.lower()
        cleaned_data.append(f"{name},{age},{email}\n")

with open("Cleaned Data.csv", 'w') as f:
    f.write("Name,Age,Email\n")
    f.writelines(cleaned_data)

print("Data cleaning complete. Cleaned file saved as 'Cleaned Data.csv'")