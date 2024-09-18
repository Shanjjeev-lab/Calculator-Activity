
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x // y

print("Addition: ", add(x,y))
print("Subtraction: ", subtract(x,y))
print("Multiplication: ", multiply(x,y))
print("Division: ", divide(x,y))
