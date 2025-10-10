while True:
    phone = input("Enter your 10-digit phone number: ")

    if len(phone) == 10 and phone.isdigit():
        print("\nPhone number saved:", phone)
        break
    else:
        print("Invalid number. Please try again\n")