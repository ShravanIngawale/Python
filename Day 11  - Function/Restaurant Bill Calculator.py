def calculator_bill(amount):
    # Add 10% service charge
    service_charge = (10 / 100) * amount
    total = amount + service_charge

    # Check if discount applies
    if total > 1000:
        discount = (5 / 100) * total
        total = total - discount

    print("Final Bill Amount:", total)

calculator_bill(900)
calculator_bill(500)
calculator_bill(1200)
calculator_bill(1300)