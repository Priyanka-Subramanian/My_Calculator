import re

print("MY CALCULATOR")
print("Type quit to exit")

run = True
previous = 0

def math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter the equation")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("BYE")
        run = False
    else:
        equation = re.sub('[a-zA-Z.():]', ' ', equation)

    if previous == 0:
        previous = eval(equation)
    else:
        previous = eval(str(previous) + equation)

    print("The result is:", previous)

while run:
    math()
