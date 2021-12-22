def calculator ():

    value1 = None
    value2 = None
    option = None
    notNumber = False
    menu = "Choose your option: \n(+) - Sum\n(-) - Subtraction\n(*) - Multiplication\n(/) - Division\n: "

    try:
        value1 = float(input("Type the first value: "))
        option = input(menu)
        value2 = float(input("Type the second value: "))

        if option == "+":
            result = (value1 + value2)
        elif option == "-":
            result = value1 - value2
        elif option == "*":
            result = (value1 * value2)
        elif option == "/":
            result = value1 / value2

        print(f"Your result is: {result}")

    except:
        notNumber = True

    if value2 == 0:
        print("Can't divide by 0")
    elif notNumber:
        print("That's not a number!")
    elif result is None:
        print("Invalid option!")
    else:
        calcString = f'{value1} {option} {value2} == {result}'
        history.append(calcString)

history = []
seeMenu = "y"
while seeMenu == "y":
    optionMenu = input("(1) If you wish to see the history of operations\n(2) If you wish to remake a operation\n(3) If you want to make a new operation\n:")

    while optionMenu != "1" and optionMenu != "2" and optionMenu != "3":
        optionMenu = input("(1) If you wish to see the history of operations\n(2) If you wish to remake an operation\n(3) If you want to make a new operation\n:")
    if optionMenu == "3":
        calculator()
    elif (optionMenu == "1" or optionMenu == "2") and len(history) == 0:
        print("No history to show!")
    elif optionMenu == '2':
        try:
            entry = int(input(f'Insert history entry ID from 0 to {len(history) - 1}:'))
            if 0 <= entry < len(history):
                print(f'[{entry}]: {history[entry]}')
            else:
                print('Out of range!')
        except:
            print('It\'s not a number!')
    else:
        for i in range(0, len(history)):
            print(f"[{i}]: {history[i]}")
    seeMenu = input("Do you wish to see the menu again? (y|n)\n:")
    if seeMenu != "y" and seeMenu != "n":
        seeMenu = input("Do you wish to see the menu again? (y|n)\n")