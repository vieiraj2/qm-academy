#Challenge 4 - Ana & Mari


def operation():
   result = None
   is_denominator_zero = False
      operator = input('''\nChoose the type of operation you want:
         '+' Sum
         '-' Subtraction
         '*' Multiplication
         '/' Division\n''')
      if operator == '+':
         is_denominator_zero = True
      elif operator == '/':
         result = n1 / n2
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

is_calculator_on = True
history = []


while is_calculator_on:
   option = input('Show Full History (\'h\'), Show History Entry (\'e\') or Make Operation (\'o\')\n').lower()
   while option != 'h' and option != 'e'and option != 'o':
      option = input('Show Full History (\'h\'), Show History Entry (\'e\') or Make Operation (\'o\')\n').lower()
   if option == 'o':
      operation()
         else:
            print('Out of range!')
      except:
         print('It\'s not a number!')
   else:
      for i in range(0, len(history)):
         print(f'[{i}]: {history[i]}')
   answer = input('Do you want to go back to menu? (Y/N)\n').lower()
   while answer != 'y' and answer != 'n':