#!/usr/bin/env python3
# Program to create a Calculator for integer numbers - Addition, Subtraction, Multiplication and Division
continua = True
while continua:
    oper_valids = False
    oper1 = oper2 = 1
    print('*** CALCULATOR FOR INTEGER VALUES ***')
 #   print('\n')
    print('1 - Addition')
    print('2 - Subtraction')
    print('3 - Multiplication')
    print('4 - Division')
    print('5 - Quit')
    operacao = input('Type the option of operation, and after press <ENTER>: ')
    print('\n')
    if  operacao == '5':
        continua = False
        continue
    elif  operacao == '1':
        print('* Addition *')
        try:
            oper1 = int(input('Input the first operator, and after press <ENTER>: '))
            oper2 = int(input('Input the first operator, and after press <ENTER>: '))
            print('Result of operation: ', oper1 + oper2)
        except:
            print('Invalid input(s)!')
    elif operacao == '2':
        print('* Subtraction *')
        try:
            oper1 = int(input('Input the first operator, and after press <ENTER>: '))
            oper2 = int(input('Input the first operator, and after press <ENTER>: '))
            print('Result of operation: ', oper1 - oper2)
        except:
            print('Invalid input(s)!')
    elif operacao == '3':
        print('* Multiplication *')
        try:
            oper1 = int(input('Input the first operator, and after press <ENTER>: '))
            oper2 = int(input('Input the first operator, and after press <ENTER>: '))
            print('Result of operation: ', oper1 * oper2)
        except:
            print('Invalid input(s)!')
    elif operacao == '4':
        print('* Division *')
        try:
            oper1 = int(input('Input the first operator, and after press <ENTER>: '))
            oper2 = int(input('Input the first operator, and after press <ENTER>: '))
            if oper2 != 0:
                print('Result of operation: ', oper1 / oper2)
            else:
                print('It does not exist a division by zero!')
        except:
            print('Invalid input(s)!')
    else:
        print('Invalid option!')

    print('\n')
    resposta = input('Repeat CALCULATOR? Y/N : ')
    if resposta != "Y" and resposta != "y":
        continua = False
    print('\n')