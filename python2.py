print("Hello World!") 


a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))

if a > b and a > c:
    print(f"{a} is the largest number")
elif b > a and b > c:
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")

x = 10
y = 3.14
name = "Alice"
is_active = True
print(x, y, name, is_active)

greeting = "Hello, World!"

print(greeting[0])
print(greeting[0:5])
print(greeting.lower())
print(greeting.upper())
print(greeting.replace("World", "Python"))

name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the world of Python")

age = int(input("Enter your age: "))
if age < 13:
    print("You are a child")
elif age >= 13 and age <= 19:
    print("You are a teenager")
else:
    print("You are a adult")


score = int(input("Enter your scorer: "))

if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("E")
