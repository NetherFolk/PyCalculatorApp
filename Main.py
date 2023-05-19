print("==Python Calculator App v0.1==")
print("Made by https://github.com/BlitzSlayerYT")

while True:

    print()
    num1 = int(input("input the first number > "))
    num2 = int(input("input the second number > "))
    action = input("Calculation(add,sub,times,divide) > ")
    print()

    add = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2

    if action == "add":
        print("result =", add)
        print()
    elif action == "sub":
        print("result =", subtraction)
        print()
    elif action == "times":
        print("result =", multiplication)
        print()
    elif action == "divide":
        print("result =", division)
        print()
    else:
        print("That operation doesn't exist")
        print()

    exit = input("Do you want to exit?(Y/N) > ")
    if exit == "Y":
        break
    else:
        continue