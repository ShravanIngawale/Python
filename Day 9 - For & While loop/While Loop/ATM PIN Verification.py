correct_pin = "2000"
attempts = 0

while attempts < 3:
    pin = input("Enter your ATM PIN: ")
    if pin == correct_pin:
        print("\n✅ Access Granted! Welcome to your account.")
        attempts = 3
    else:
        print("\n❌ Wrong PIN! Try again.\n")
        attempts = attempts + 1