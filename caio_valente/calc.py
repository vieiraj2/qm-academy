def calculator ():

    denominatorIs0 = None
    value1 = None
    value2 = None
    option = None
    notNumber = False
    menu = "Choose your option: \n +    -\n *    /\n: "

    try:
        value1 = float(input("Type the first value: "))
        option = input(menu)
        value2 = float(input("Type the second value: "))

        if (option == "+"):
            result = (value1 + value2)
        elif (option == "-"):
            result = value1 - value2
        elif (option == "*"):
            result = (value1 * value2)
        elif (option == "/"):
            result = value1 / value2

        print(f"Your result is: {result}")

    except:

        print("Something went wrong, try again!")


        if value2 == 0:
           print("Can't divide by 0")

sair = "0"
while sair == "0":
    calculator()
    sair = input("Do you wish to quit? Yes = Any value | No = 0\n")