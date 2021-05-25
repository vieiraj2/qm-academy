import sys

def linha():
    print('-'*70)


def calculadora():
    linha()
    while True:
        try:
            n1 = float(input('Primeiro valor: '))
            linha()
            n2 = float(input('Segundo valor: '))
            linha()
        except(ValueError, TypeError):
            print('ERRO: Por favor, digite um número válido!')
            continue

        opção = 0
        while opção != 6:
            try:
                print(''' 
                    [ 1 ] Somar
                    [ 2 ] Subtrair
                    [ 3 ] Multiplicar
                    [ 4 ] Dividir
                    [ 5 ] Inserir os valores novamente
                    [ 6 ] Sair
                    ''')
                linha()
                opção = int(input('>>>>> Digite sua opção: '))
                linha()
            except(ValueError, TypeError):
                print('ERRO: Por favor, digite um número válido!')
                continue

            if opção == 1:
                soma = n1 + n2
                print('A soma entre {} e {} é {}'.format(n1, n2, soma))
            elif opção == 2:
                produto = n1 - n2
                print('A subtração de {} e {} é {}'.format(n1, n2, produto))
            elif opção == 3:
                vezes = n1 * n2
                print('A multiplicação de {} e {} é {}'.format(n1, n2, vezes))
            elif opção == 4:
                if n1 and n2 > 0:
                    divisao = n1 / n2
                    print('A divisao de {} e {} é {}'.format(n1, n2, divisao))
                else:
                    print('Não podemos operar divisão 0')
            elif opção == 5:
                print('Informe os números novamente: ')
                n1 = int(input('Primeiro valor: '))
                n2 = int(input('Segundo valor: '))
            elif opção == 6:
                print('Finalizando....')
                sys.exit()
            else:
                print('Opção inválida, tente novamente')


calculadora()
