### Introdução - Menu
continua = True
while continua:
    print('Olá, Selecione a opção abaixo')
    print(' 1 Soma de dois números (+)'
      '\n 2 Subtração entre dois números (-)'
      '\n 3 Multiplicação de dois números (*)'
      '\n 4 Divisão de dois números  (/)')

##### Segundo passo
    num = input('Digite uma opção:')
    if num =='1':
       print('Opção Soma Selecionada')
       try:
         num1 = int(input('Digite o primeiro numero'))
         num2 = int(input('Digite o segundo numero'))
         print('Resultado: {} '.format(num1 + num2))
       except:
         print ('Digite um numero valido')

    elif num == '2':
        print('Opção subtração selecionada')
        try:
            num1 = int(input('Digite o primeiro numero'))
            num2 = int(input('Digite o segundo numero'))
            print('Resultado: {} '.format(num1 - num2))
        except:
            print ('Digite um numero valido')

    elif num == '3':
        print('Opção Multiplicação selecionada')
        try:
            num1 = int(input('Digite o primeiro numero'))
            num2 = int(input('Digite o segundo numero'))
            print('Resultado: {} '.format(num1 * num2))
        except:
            print ('Digite um numero valido')

    elif num == '4':
        print('Opção Divisão selecionada')
        try:
            num1 = int(input('Digite o primeiro numero'))
            num2 = int(input('Digite o segundo numero'))
            if num2 != 0:
                print('Resultado: {} '.format(num1 / num2))
            else:
                print('erro')
        except:
            print ('Digite um numero valido')

    elif num =='':
        print('Selecione uma opção valida')

    else:
        print('Digite um numero valido')

    final = input('Deseja finalizar? Y/N:')
    if final =='y' or final =='Y':
        continua = False













