a = 60
b = 7
a + b
a - b
a * b
print(a / b)
print(a // b)
print(a % b)
print(6 ** 2)
print(6 ** 0.5)
x, y = divmod(a, b)
print('x=', x)
print('y=', y)

c = float(input("c = "))
d = float(input("d = "))
e = c + d
print('c + d =', e)
name = input("What is your name?")

len = 5
my_second_number = 10
print(len + my_second_number)
print(len('hello'))

# True va False
# >, <, ==, <=, >=, !=
# == tengmi?
f = 4
g = 15
# print(f != g) # print(False)
print(bool(0))
print(bool(1))
print('Stringlar uchun')
print(bool(""))
print(bool("asdf"))
print("Boolean uchun")
print(bool(True))
print(bool(False))
print("Container data typelar uchun")
print(bool([])) # Empty List
print(bool([1, 2])) # List
print(bool(tuple())) # Empty Tuple
print(bool((1, 2))) # Tuple
print(bool({})) # Emple Dictionary
print(bool({"key": "value"})) # Dictionary
print(bool(set())) # Emple Set
print(bool({1, 2, 3})) # Set
print("-"*20)
print(bool(" "))

word = input()
if not bool(word.strip()):
    print("Please enter somethinng")
else:
    print("You entered:", word)   