#!/usr/bin/env python3
# Program to create a Calculator for integer numbers - Addition, Subtraction, Multiplication and Division
# With IMPROVEMENTS - History of operations
continua = True     # variavel de controle do loop principal WHILE
Historic = []      # Lista p/ armazenamento de informações de operações para Histórico
while continua:
    oper_valids = False
    oper1 = oper2 = 1
    print('*** CALCULATOR FOR INTEGER VALUES ***')
 #   print('\n')
    print('1 - Addition')
    print('2 - Subtraction')
    print('3 - Multiplication')
    print('4 - Division')
    print('5 - Historic of Operations')
    print('6 - Quit')
    operacao = input('Type the option of operation, and after press <ENTER>: ')
    print('\n')
    if  operacao == '6':
        continua = False
        continue
    elif  operacao == '5':
        if len(Historic) == 0:
            print('Historic of Operations is empty!')
            print('\n')
            continue
        print('** Historic of Operations **')
        #   print('\n')
        print('1 - All Operations')
        print('2 - Choose a specific operation')
        print('3 - Return')
        option_hist = input('Type the option for Historic, and after press <ENTER>: ')

        if option_hist == '1':
            print('EXIBIR TODO HISTORICO')
            for j in range(len(Historic)):
                #print('Operation ', j+1, ': ', Historic[j])
                print(Historic[j])
                print('\n')
        elif option_hist == '2':
            try:
                option_oper = int(input('Type which operation would you like to search: '))
            except:
                print('Invalid input(s)!')
                print('\n')
                continue
            if option_oper != 0:
                print(Historic[option_oper - 1])
                print('\n')
            else:
                print('Invalid input(s)!')
        else:
            print('\n')
            continue

    elif  operacao == '1':
        print('* Addition *')
        try:
            oper1 = int(input('Input the first operator, and after press <ENTER>: '))
            oper2 = int(input('Input the second operator, and after press <ENTER>: '))
        except:
            print('Invalid input(s)!')
            print('\n')
            continue
        print('Result of operation: ', oper1 + oper2)
        # GUARDA NO HISTORICO
        resultado = oper1 + oper2
        content = (oper1, " + ", oper2, ' = ', resultado)
        Historic.append(content)
        print('\n')

    elif operacao == '2':
        print('* Subtraction *')
        try:
            oper1 = int(input('Input the first operator, and after press <ENTER>: '))
            oper2 = int(input('Input the second operator, and after press <ENTER>: '))
        except:
            print('Invalid input(s)!')
            print('\n')
            continue
        print('Result of operation: ', oper1 - oper2)
        # GUARDA NO HISTORICO
        resultado = oper1 - oper2
        content = (oper1, " - ", oper2, ' = ', resultado)
        Historic.append(content)
        print('\n')

    elif operacao == '3':
        print('* Multiplication *')
        try:
            oper1 = int(input('Input the first operator, and after press <ENTER>: '))
            oper2 = int(input('Input the second operator, and after press <ENTER>: '))
        except:
            print('Invalid input(s)!')
            print('\n')
            continue
        print('Result of operation: ', oper1 * oper2)
        # GUARDA NO HISTORICO
        resultado = oper1 * oper2
        content = (oper1, " * ", oper2, ' = ', resultado)
        Historic.append(content)
        print('\n')

    elif operacao == '4':
        print('* Division *')
        try:
            oper1 = int(input('Input the first operator, and after press <ENTER>: '))
            oper2 = int(input('Input the second operator, and after press <ENTER>: '))

        except:
            print('Invalid input(s)!')
            print('\n')
            continue
        if oper2 != 0:
            print('Result of operation: ', oper1 / oper2)
        else:
            print('It does not exist a division by zero!')
            print('\n')
            continue
        # GUARDA NO HISTORICO
        resultado = oper1 / oper2
        content = (oper1, " / ", oper2, ' = ', resultado)
        Historic.append(content)
        print('\n')

    else:
        print('Invalid option!')

    print('\n')
    resposta = input('Repeat CALCULATOR? Y/N : ')
    if resposta != "Y" and resposta != "y":
        continua = False
    print('\n')