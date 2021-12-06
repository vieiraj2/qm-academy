def calculator ():

    denominatorIs0 = None
    value1 = None
    value2 = None
    option = None
    menu = "Choose your option: \n +    -\n *    /\n"

    value1 = float(input("Type the first value: "))
    option = input(menu)
    value2 = float(input("Type the second value: "))
    try:
        if (option == "+"):
            result = (value1 + value2)
        elif (option == "-"):
            result = value1 - value2
        elif (option == "*"):
            result = (value1 * value2)
        elif (value2 == 0):
            denominatorIs0 == True
        elif (option == "/"):
            result = value1 / value2

        print("Your result is: {}".format(result))

    except:
       if (denominatorIs0 == True):
           print("Can't divide by 0")

sair = 0
while sair == 0:
    calculator()
    sair = input("Do you wish to quit? Yes = Any value | No = 0\n")