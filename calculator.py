"""
def add(a, b):
    c = a + b
    return c, "+"


def subtract(a, b):
    c = a - b
    return c, "-"


def multiply(a, b):
    c = a * b
    return c, "*"


def divide(a, b):
    c = a / b
    return c, "/"


a, b = 47, 7
print("{} {} {} = {}".format(a, add(a,b)[1], b, add(a, b)[0]))
"""


def add(a, b):
    c = a + b
    return c, "+"


def subtract(a, b):
    c = a - b
    return c, "-"


def multiply(a, b):
    c = a * b
    return c, "*"


def divide(a, b):
    c = a / b
    return c, "/"


inp = input("Input letter to define operation: ")
num1 = float(input("enter number 1: "))
num2 = float(input("enter number 2: "))
print("You entered {}".format(inp))
if inp == "a":
    d = add(num1, num2)
elif inp == "s":
    d = subtract(num1, num2)
elif inp == "m":
    d = multiply(num1, num2)
elif inp == "d":
    d = divide(num1, num2)
else:
    print("The {} command is not recognized.".format(inp))

print("{} {} {} = {}".format(num1, d[1], num2, d[0]))