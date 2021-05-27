import itertools
import sys


def line():
    print('-' * 80)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def calculate():
    for c in itertools.count(start=0):
        history = []
        while True:
            try:
                line()
                num1 = float(input("Enter first number: "))
                line()
                num2 = float(input("Enter second number: "))
            except(ValueError, TypeError):
                print('INVALID INPUT')
                line()
                continue
            choice = 0
            while choice != 6:
                try:
                    line()
                    print('''CHOOSE YOUR OPTIONS:
                                    [ 1 ] ADD
                                    [ 2 ] SUBTRACT
                                    [ 3 ] MULTIPLY
                                    [ 4 ] DIVIDE
                                    [ 5 ] INPUT THE NUMBERS AGAIN
                                    [ 6 ] HISTORY
                                    [ 7 ] EXIT''')
                    line()
                    choice = input("Enter choice: ")

                    if choice in ('1', '2', '3', '4', '5', '6', '7'):

                        if choice == '1':
                            line()
                            print(num1, "+", num2, "=", add(num1, num2))
                            c += 1
                            history.append({'num1': num1, 'num2': num2, 'choice': 'add', 'position': c})

                        elif choice == '2':
                            line()
                            print(num1, "-", num2, "=", subtract(num1, num2))
                            c += 1
                            history.append({'num1': num1, 'num2': num2, 'choice': 'subtract', 'position': c})

                        elif choice == '3':
                            line()
                            print(num1, "*", num2, "=", multiply(num1, num2))
                            c += 1
                            history.append({'num1': num1, 'num2': num2, 'choice': 'multiply', 'position': c})

                        elif choice == '4':
                            line()
                            print(num1, "/", num2, "=", divide(num1, num2))
                            c += 1
                            history.append({'num1': num1, 'num2': num2, 'choice': 'divide', 'position': c})

                        elif choice == '5':
                            line()
                            num1 = float(input("Enter first number: "))
                            num2 = float(input("Enter second number: "))

                        elif choice == '6':
                            line()
                            print(''' HISTORY:
                                    Press 1 if you wanna see all history
                                    Press 2 if you wanna see just a position
                                    ''')
                            line()
                            choice1 = int(input("Enter choice: "))

                            if choice1 == 1:
                                line()
                                print(history)
                            elif choice1 == 2:
                                line()
                                position_hist = int(input('What position do you want? '))
                                if len(history) >= position_hist > 0:
                                    position_hist -= 1
                                    line()
                                    print(history[position_hist])
                            else:
                                line()
                                print('INVALID INPUT')

                        elif choice == '7':
                            line()
                            print('Thank you....')
                            line()
                            sys.exit()

                except(ValueError, TypeError):
                    line()
                    print('INVALID INPUT')


calculate()
