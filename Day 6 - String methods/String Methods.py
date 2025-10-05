a = "on mission! to master python!!!"
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("mission", "journey"))
print(a.split(" "))
print(a.capitalize())
print(a.center(62))
print(a.count("on"))
print(a.endswith("!!!"))
print(a.endswith("to", 10, 14))
print(a.find("on")) # -1
print(a.index("on")) # error

b = "MasterPython100Days"
print(b.isalnum())
print(b.isalpha())

print(a.islower())

c = "Hi\nHi"
print(c.isprintable())

d = " "
print(d.isspace())

a1 = "Hello Python World"
print(a1.istitle())

a2 = "HELLO WORLD"
print(a2.isupper())

print(a.startswith("on"))
print(a.startswith("mission", 3))

a3 = "Hello World"
print(a3.swapcase())

print(a.title())