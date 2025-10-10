total = 0
count = 0

print("Enter marks of 5 students (enter -1 if absent):")

for i in range(5):
    marks = int(input("Enter marks: "))
    if marks == -1:
        continue
    total = total + marks
    count = count + 1

if count > 0:
    average = total / count
    print("\nAverage marks of present student is:", round(average,2))
else:
    print("\nNo student was present!")