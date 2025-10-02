a = 10
b = 3.5
c = a + b
print(c)
print(type(c), "\n")

x = True        # bool ----> treated as 1
y = 5              # int 
result = x + y
print(result)
print(type(result), "\n")

x = False     # bool ----> treated as 0
y = 4.2         # float
z = x + y
print(z)
print(type(z), "\n")

a = 5 + 3j     # complex
b = 2             # int 
result = a + b
print(result)
print(type(result), "\n")

x = 10
y = 4
z = x / y
print(z)
print(type(z), "\n")

print(type(10 + 2.0)) # float
print(type(10 + True)) # int
print(type(10 / 2)) # float
print(type(False + 3.0)) # float