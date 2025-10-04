text = "PythonProgramming"

print(text[:6])
print(text[6:])
print(text[4:9])

print(text[-6:]) # 17-6=11
print(text[:-3]) # 17-3 14

print(text[0: :2 ])
print(text[: :-1])
print(text[6:][::-1])
print(text[:6] + text[6:][::-1])
print(text[:6][::-1] + text[6:])

#a = input("\nEnter a word: ")
#print(a[:len(a)//2])
#print(a[len(a)//2:])
#print(a[::-1])
print()
text = "DataScience"
print(text[:4])
print(text[4:])
print(text[1:8])
#print(len(text))