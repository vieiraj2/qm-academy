import itertools
from calculator_concat_sum import CalculatorConcatSum

for g in itertools.count(start=0, step=1):

    #initial banner
    def initial_banner():
        print("\033[2m" + "\033[96m" + '\n' + "-" * 62 + '\n' + '\n' + '#' * 62 + '\n' + '#' * 25 +
              ' CALCULATOR ' + '#' * 25 + '\n' + '#' * 62
              + '\n' + '\n' + 'Enter 1st number > Then enter the operation > Enter 2nd number' + '\n')


    def line2():
        print('\n' + "\033[2m" + "\033[39m" + "-" * 62 + '\n')


    initial_banner()

    # calc counter
    if g == 0:
        print("\033[2m" + "\033[39m" + 'This is the execution number: 1')
        result_list = []
    else:
        print("\033[2m" + "\033[39m" + 'This is the execution number: {}'.format(g+1))

    # calc history
    while True:
        if g != 0:
            line2()
            hist = input("\033[2m" + "\033[34m" + 'Do you want to see calc history?\n'
                                                  '1. Yes / 2. No, keep calculating: ')
            if hist == '1':
                while True:
                    line2()
                    hist2 = input("\033[2m" + "\033[34m" +
                                  'Choose one option:\n1. All calc history / 2. One specific calc: ')
                    if hist2 == '1':
                        line2()
                        print("\033[2m" + "\033[39m" + 'Calc history:')
                        print(result_list)
                        break
                    elif hist2 == '2':
                        hist3 = ''
                        while True:
                            try:
                                line2()
                                hist3 = int(input("\033[2m" + "\033[34m" + 'Input calc number # : '))
                                print(result_list[hist3-1])
                                break
                                line2()
                            except (ValueError, IndexError):
                                line2()
                                hist2 == '2'
                                print("\033[1m" + "\033[31m" + 'ERROR! This input is not on the calc list or '
                                                               'is not valid'.format(hist3))
                        break
                    else:
                        line2()
                        print("\033[1m" + "\033[31m" + 'ERROR! Insert valid option: "1" or "2"')
            elif hist == '2':
                break
            else:
                line2()
                print("\033[1m" + "\033[31m" + 'ERROR! Insert valid option: "1" or "2"')
        else:
            break

    # enter 1st number
    v1 = True
    while v1:
        try:
            line2()
            a = float(input("\033[2m" + "\033[39m" + "Enter 1st number: "))
            v1 = False
        except ValueError:
            line2()
            print("\033[1m" + "\033[31m" + 'ERROR! Digit a valid 1st number!')

    # enter operation
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

    # enter second number
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

    # operations
    calculator = CalculatorConcatSum(a, b)

    if op == "+":
        result = calculator.addition()
        result_list.append('Calc {}: '.format(g+1) + str(a) + " " + str(op) + " " + str(b) + " = " + str(result))
        #print("\033[1m" + "\033[32m" + 'Result: ' + str(a) + " " + str(op) + " " + str(b) + " = " + str(result))
    elif op == "-":
        result = calculator.sub()
        result_list.append('Calc ' + str(g+1) + ': ' + str(a) + " " + str(op) + " " + str(b) + " = " + str(result))
        print("\033[1m" + "\033[32m" + 'Result: ' + str(a) + " " + str(op) + " " + str(b) + " = " + str(result))
    elif op == "*":
        result = calculator.multiply()
        result_list.append('Calc ' + str(g+1) + ': ' + str(a) + " " + str(op) + " " + str(b) + " = " + str(result))
        print("\033[1m" + "\033[32m" + 'Result: ' + str(a) + " " + str(op) + " " + str(b) + " = " + str(result))
    elif op == "/":
        result = calculator.divide()
        result_list.append('Calc ' + str(g+1) + ': ' + str(a) + " " + str(op) + " " + str(b) + " = " + str(result))
        print("\033[1m" + "\033[32m" + 'Result: ' + str(a) + " " + str(op) + " " + str(b) + " = " + str(result))

    # keep calc or not
    line2()
    v3 = True
    while v3:
        program = input("\033[2m" + "\033[34m" + 'Do you want to make other calc?\n1. Yes / 2. No: ')
        if program == '1':
            v3 = False
        elif program == '2':
            v3 = False
            line2()
            print("\033[2m" + "\033[39m" + 'All calc executions made during this session:')
            print(result_list)
            line2()
            print("\033[1m" + "\033[93m" + "Calculator is finished. Thank you xD")
            line2()
            exit()
        else:
            line2()
            print("\033[1m" + "\033[31m" + 'ERROR! Insert valid option: "1" or "2"')
            line2()
            v3 = True
