with open("Feedback.txt", 'w') as f:
    feedback = [
        "Great service!\n"
        "Very satisfied with the product\n"
        "Delivery was super fast\n"
        "Packaging could be improved\n"
        "Customer support was helpful"
    ]
    f.writelines(feedback)

with open("Feedback.txt", 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()

    print("First customer feedback:", line1)
    print("Second customer feedback:", line2)
    print("Third customer feedback:", line3)