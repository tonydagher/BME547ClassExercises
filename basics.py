# basics
x = input("Enter a letter: ")
# print("You entered {}".format(x))
# print("This is a line of code.")
if x == "a":
    a = 1
    b = 2
    c = a+b
    print("{} + {} = {}".format(a, b, c))
elif x == "s":
    a = 20
    b = -3
    c = a - b
    print("{} - {} = {}".format(a, b, c))
elif x == "m":
    a = 4
    b = 5
    c = a*b
    print("{} x {} = {}".format(a, b, c))
else:
    print("The {} command is not recognized.".format(x))
print("Done")
