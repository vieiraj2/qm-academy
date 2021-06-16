# Introdução - Menu
continua = True
Historico = []
while continua:
    print('Calculadora!, Selecione a opção abaixo')
    print(' 1 Soma de dois números (+)'
          '\n 2 Subtração entre dois números (-)'
          '\n 3 Multiplicação de dois números (*)'
          '\n 4 Divisão de dois números  (/)'
          '\n 5 Histórico')

    # Seleção_Histórico!

    num = input('Digite uma opção:')
    if num == '1':
        print('Opção Soma Selecionada')
        try:
            num1 = int(input('Digite o primeiro numero'))
            num2 = int(input('Digite o segundo numero'))
            print('Resultado: {} '.format(num1 + num2))
            # Histórico_registro soma
            resultado = num1 + num2
            his = (num1, '+', num2, '=', resultado)
            Historico.append(his)
        except:
            print('Digite um numero valido')

    # Seleção_Subtração
    elif num == '2':
        print('Opção subtração selecionada')
        try:
            num1 = int(input('Digite o primeiro numero'))
            num2 = int(input('Digite o segundo numero'))
            print('Resultado: {} '.format(num1 - num2))
            # Histórico - registro subtração
            resultado = num1 - num2
            his = (num1, '-', num2, '=', resultado)
            Historico.append(his)
        except:
            print('Digite um numero valido')
    # Seleção_Multiplicação
    elif num == '3':
        print('Opção Multiplicação selecionada')
        try:
            num1 = int(input('Digite o primeiro numero'))
            num2 = int(input('Digite o segundo numero'))
            print('Resultado: {} '.format(num1 * num2))
            # Histórico_registro_multiplicação
            resultado = num1 * num2
            his = (num1, '*', num2, '=', resultado)
            Historico.append(his)
        except:
            print('Digite um numero valido')
    # Seleção_Divisão
    elif num == '4':
        print('Opção Divisão selecionada')
        try:
            num1 = int(input('Digite o primeiro numero'))
            num2 = int(input('Digite o segundo numero'))
            if num2 != 0:
                print('Resultado: {} '.format(num1 / num2))
            else:
                print('erro - Não pode ser dividido por zero! ')
                # Histórico - registro divisão
                resultado = num1 / num2
                his = (num1, '/', num2, '=', resultado)
                Historico.append(his)
        except:
            print('Digite um numero valido')

    # validação para vazio!
    elif num == '':
        print('Selecione uma opção valida')
        continue
    elif num == '5':
        if len(Historico) == 0:
            print('Histórico de operações está vazio!!')
            continue

        # Menu de Seleção
        print('Histórico de Operações')
        print('1 - Todas as Operações')
        print('2 - Escolha uma operação específica')

        # Seleção de opções
        opcao_hist = input('Selecione uma das opções:')
        if opcao_hist == '1':
            print('Exibir todo o histórico')
            for h in range(len(Historico)):
                print(Historico[h])
                print('\n')
        elif opcao_hist == '2':
            try:
                oper = int(input('Digite qual operação você gostaria de pesquisar'))
            except:
                print('Opção invalida!')
                print('\n')
                continue
            if oper != 0:
                print(Historico[oper - 1])
            else:
                print('Opção invalida!')
    else:
        print('Digite um numero valido')

    final = input('Deseja finalizar? Y/N:')
    if final == 'y' or final == 'Y':
       continua = False
