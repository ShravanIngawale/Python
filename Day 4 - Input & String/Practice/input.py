#a = input("Enter something: ")
#print(a)

#name = input("Enter your name: ")
#print("Good Morning,", name + "!")

#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
#print("Sum is:", a + b)

#age = int(input("Enter your age: "))
#print("Next year you will be", age + 1)

#food = input("What's your favorite food? ")
#print("Wow! I Iove", food, "too!")

#name = input("What is your name? ")
#age = input("How old are you? ")
#print("Hello", name, "you are", age, "years old.")

#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))
#print("Sum is:", num1 + num2)
#print("Product is:", num1 * num2)

#movie = input("Enter your favorite movie: ")
#rating = input("Rate it out of 10: ")
#print("You rated", movie, "a", rating + "/10!")

#num = int(input("Enter a number: "))
#print("Square is:", num ** 2)
#print("Cube is:", num ** 3)

#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))
#avg = (num1 + num2 + num3) / 3
#print("Average is:", avg)

#len = float(input("Enter length: "))
#wid = float(input("Enter width: "))

#area = len * wid
#peri = 2 * (len + wid)

#print("Area of Rectangle is:", area)
#print("Perimeter of Rectangle is:", peri)

#num1 = int(input("Enter dividend: "))
#num2 = int(input("Enter divisor: "))

#print("Quotient is:", num1 // num2)
#print("Remainder is:", num1 % num2)

#a = int(input("Enter first number: ")) 
#b = int(input("Enter second number: "))

#a, b = b, a

#print("After swapping: ")
#print("First number:", a)
#print("Second number:", b)

#cm = float(input("Enter length in cm: "))
#print("Meters:", cm / 100)
#print("Kilometers:", cm / 100000)

#seconds = int(input("Enter seconds: "))    	
#hours = seconds // 3600
#min = (seconds % 3600) // 60
#sec = seconds % 60
#print(hours, "Hours,", min, "Minutes,", sec, "Seconds")

# Simple Interest Calculator
P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time in years: "))

SI = (P * R * T) / 100
print("Simple Interest is:", SI)