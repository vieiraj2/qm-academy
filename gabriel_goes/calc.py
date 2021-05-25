run = True

while run:

    def initial_banner():
        print("\033[2m" + "\033[96m" + '\n' + "-" * 62 + '\n' + '\n' + '#' * 62 + '\n' + '#' * 25 +
              ' CALCULATOR ' + '#' * 25 + '\n' + '#' * 62
              + '\n' + '\n' + 'Enter 1st number > Then enter the operation > Enter 2nd number')


    def line2():
        print('\n' + "\033[2m" + "\033[39m" + "-" * 62 + '\n')


    initial_banner()

    v1 = True
    while v1:
        try:
            line2()
            a = float(input("\033[2m" + "\033[39m" + "Enter 1st number: "))
            v1 = False
        except ValueError:
            line2()
            print("\033[1m" + "\033[31m" + 'ERROR! Digit a valid 1st number!')

    op_er = True
    while op_er:
        line2()
        op = input("\033[2m" + "\033[39m" + 'Operations available:\n"+" \n"-" \n"*" \n"/"' +
                   '\nInput the operation here: ')
        if op == "+" or op == "-" or op == "*" or op == "/":
            op_er = False
        else:
            line2()
            print("\033[1m" + "\033[31m" + "ERROR! Digit a valid operation")

    v2 = True
    while v2:
        try:
            line2()
            b = float(input("\033[2m" + "\033[39m" + "Enter 2nd number: "))
            if op == "/" and b == 0:
                line2()
                print("\033[1m" + "\033[31m" + "ERROR! Not possible to divide by zero! Try other number")
            else:
                v2 = False
        except ValueError:
            line2()
            print("\033[1m" + "\033[31m" + "ERROR! Digit a valid 2nd number!")
    line2()


    def addition():
        result = a + b
        print("\033[1m" + "\033[32m" + 'Result: ' + str(a) + " " + str(op) + " " + str(b) + " = " + str(result))


    def sub():
        result = a - b
        print("\033[1m" + "\033[32m" + 'Result: ' + str(a) + " " + str(op) + " " + str(b) + " = " + str(result))


    def multiplication():
        result = a * b
        print("\033[1m" + "\033[32m" + 'Result: ' + str(a) + " " + str(op) + " " + str(b) + " = " + str(result))


    def div():
        result = a / b
        print("\033[1m" + "\033[32m" + 'Result: ' + str(a) + " " + str(op) + " " + str(b) + " = " + str(result))


    if op == "+":
        addition()
    elif op == "-":
        sub()
    elif op == "*":
        multiplication()
    elif op == "/":
        div()

    line2()
    v3 = True
    while v3:
        program = input("\033[2m" + "\033[34m" + 'Do you want to make other calc?\n1. Yes / 2. No: ')
        if program == '1':
            run = True
            v3 = False
        elif program == '2':
            run = False
            v3 = False
            line2()
            print("\033[1m" + "\033[93m" + "Calculator is finished. Thank you xD")
            line2()
        else:
            line2()
            print("\033[1m" + "\033[31m" + 'ERROR! Insert valid option: "1" or "2"')
            line2()
            v3 = True