#Challange 3 - Team 4 - Sergio e Janine

print('\033[35m'+'\n*****************************'+'\033[0;0m')
print('\033[35m'+'\n*********CALCULADORA*********'+'\033[0;0m')
print('\033[35m'+'\n*****************************'+'\033[0;0m')

n1 = 0
n2 = 0
result = 0

while True:
    
    operacao = input('\nBem-vindo! Você pode fazer 4 tipos de operações: \n\n1-Adição \n2-Subtração \n3-Multiplicação \n4-Divisão \n\nDigite qual operação deseja fazer: ')
    temp=''
    try:

        if operacao== '1':
            temp = '+'
            n1 = float(input('Digite primeiro número: '))
            n2 = float(input('Digite segundo número: '))
            result = n1 + n2

        elif operacao== '2':
            temp='-'
            n1 = float(input('Digite primeiro número: '))
            n2 = float(input('Digite segundo número: '))
            result = n1 - n2

        elif operacao== '3':
            temp = '*'
            n1 = float(input('Digite primeiro número: '))
            n2 = float(input('Digite segundo número: '))
            result = n1 * n2

        elif operacao== '4':
            temp = '/'
            n1 = float(input('Digite primeiro número: '))
            n2 = float(input('Digite segundo número: '))
            result = n1 / n2

        else:
            result = 'Opção inválida'
        print('\033[32m'+'\nResultado: '+'\033[0;0m' + str(n1) + ' ' + str(temp) + ' ' + str(n2) + ' = ' + str(result))

        op2 = input('\nPressione ENTER para continuar ou digite 0 para sair: ')
        if op2 == '0':
            print('\033[1;34m'+'\n*****SAINDO DA APLICAÇÃO*****'+'\033[0;0m')
            break
    except:
        print('\033[31m'+'\n\n------FALHA NA OPERAÇÃO------\n'+'\033[0;0m')

        op2 = input('\nPressione ENTER para continuar ou digite 0 para sair: ')
        if op2 == '0':
            print('\n*****SAINDO DA APLICAÇÃO*****')
            break