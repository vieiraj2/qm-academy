# team 1: Ana & Mari

is_calculator_on = True
while is_calculator_on:
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

      if operator == '+':
         result = n1 + n2

      elif operator == '-':
         result = n1 - n2

      elif operator == '*':
         result = n1 * n2
      
      elif operator == '/' and n2 == 0:
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
      print(f'You chose \'{operator}\'')
      print(f'{n1} {operator} {n2} = {result}')
      
   answer = input('Do you want to make another operation? (Y/N)\n').lower()
   while answer != 'y' and answer != 'n':
      answer = input('Do you want to make another operation? (Y/N)\n').lower()

   is_calculator_on = answer == 'y'