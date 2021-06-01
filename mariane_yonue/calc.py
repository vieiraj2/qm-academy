#Challenge 5 - Team 1: Ana & Mari

from calculator_concat_sum import CalculatorConcatSum


def operation():
    result = None
    is_denominator_zero = False
    not_a_number = False

    try:
        n1 = float(input('First number:'))
        n2 = float(input('Second number:'))
        operator = input('''\nChoose the type of operation you want:
            '+' Sum
            '-' Subtraction
            '*' Multiplication
            '/' Division\n''')

        calculator = CalculatorConcatSum(n1, n2)

        if operator == '+':
            result = calculator.sum()

        elif operator == '-':
            result = calculator.sub()

        elif operator == '*':
            result = calculator.mult()
        
        elif operator == '/' and n2 == 0:
            is_denominator_zero = True

        elif operator == '/':
            result = calculator.div()
    
    except:
        not_a_number = True

    if is_denominator_zero:
        print ('Can\'t divide by zero! Try again')

    elif not_a_number:
        print ('It\'s not a number!')
    
    elif result == None:
        print ('Invalid option!')
    
    else:
        operation_string = f'{n1} {operator} {n2} = {result}'
        history.append(operation_string)

is_calculator_on = True
history = []
while is_calculator_on:
    option = input('Show Full History (\'h\'), Show History Entry (\'e\') or Make Operation (\'o\')\n').lower()
    while option != 'h' and option != 'e'and option != 'o':
        option = input('Show Full History (\'h\'), Show History Entry (\'e\') or Make Operation (\'o\')\n').lower()

    if option == 'o':
        operation()

    elif (option == 'e' or option == 'h') and len(history) == 0:
        print('No history to show!')
    
    elif option == 'e':
        try:
            entry = int(input(f'Insert history entry ID from 0 to {len(history) - 1}:'))

            if entry >= 0 and entry < len(history):
                print(f'[{entry}]: {history[entry]}')

            else: 
                print('Out of range!')
        
        except:
            print('It\'s not a number!')

    else:
        for i in range(0, len(history)):
            print(f'[{i}]: {history[i]}')
        
    answer = input('Do you want to go back to menu? (Y/N)\n').lower()
    while answer != 'y' and answer != 'n':
        answer = input('Do you want to go back to menu? (Y/N)\n').lower()

    is_calculator_on = answer == 'y'