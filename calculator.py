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
print("{} + {} = {}".format(a, b, add(a, b)[0]))
"""


def add(x, y):
    z = x + y
    print("{} + {} = {}".format(x, y, z))
    return z


def subtract(x, y):
    z = x - y
    print("{} - {} = {}".format(x, y, z))
    return z


def multiply(x, y):
    z = x*y
    print("{} x {} = {}".format(x, y, z))
    return z


inp = input("enter a letter: ")
print("You entered {}".format(inp))
if inp == "a":
    d = add(56, 73)
elif inp == "s":
    d = subtract(56, 73)
elif inp == "m":
    d = multiply(56, 73)
else:
    print("The {} command is not recognized.".format(inp))