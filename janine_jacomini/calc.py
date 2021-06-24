#Challenge 3, 4 e 5 - Calculator - Team 4 - Sergio e Janine
#from calculator import Calculator #importa a classe calculator do arquivo calculator
from calculator_concat_sum import CalculatorConcatSum

print('\033[35m'+'\n***** CALCULADORA *****'+'\033[0;0m')
log_hist = []
Fim = True
result = None
ResultCalc = CalculatorConcatSum(1,2)

def refazerOper(): #função para refazer operação
    global Fim
    while True:
        op2 = input('\nDeseja fazer outra operação? Digite 1 para continuar ou  0 para sair: ')
        if op2 == '0':
            print('\n\033[7;34m' + '***** SAINDO DA APLICAÇÃO *****' + '\033[0;0m')
            Fim = False
            break
        elif op2 != '1' or '0':
            print('\n\033[7;31m' + 'ERRO! Por favor, insira uma opção válida: "1" ou "0"\033[0;0m')

while Fim:
    operacao = input('\nBem-vindo! Você pode fazer 5 tipos de operações: \n\n1-Adição \n2-Subtração \n3-Multiplicação \n4-Divisão  \n5-Histórico \n\nEscolha o tipo de operação: ')
    temp=''
    try:
        if operacao== '1':
            temp = '+'
            result = ResultCalc.sum()

        elif operacao== '2':
            temp='-'
            result = ResultCalc.sub()

        elif operacao== '3':
            temp = '*'
            result = ResultCalc.mult()

        elif operacao== '4':
            temp = '/'
            result = ResultCalc.div()

        elif operacao == '5':
            operacao_hist = input('\n1-Ultimas execuções \n2-Histórico por posição \n\nEscolha o tipo de histórico: ')
            if operacao_hist == '1':
                if len(log_hist)>0:
                    print('\n\033[1;96m----------------------------------------------\033[0;0m')
                    print('\033[1;96m Histórico \033[0;0m')
                    print('\033[1;96m----------------------------------------------\033[0;0m')
                    posicao = 1
                    for temp_hist in log_hist:
                        print('\033[1;34mOperação ' + str(posicao) +': \033[0;0m' +temp_hist)
                        posicao+=1
                    print('\033[1;96m\n----------------------------------------------\033[0;0m')
                    print('\033[1;96m Fim Histórico \033[0;0m')
                    print('\033[1;96m----------------------------------------------\033[0;0m')
                else:
                    print('\033[7;33m\nHistórico vazio\033[0;0m')
            elif operacao_hist == '2':
                posicao_hist = int(input('\nQual posição deseja? '))
                if len(log_hist) >= posicao_hist > 0:
                    posicao_escolhida = posicao_hist
                    posicao_hist-=1 #decrementando pois a lista começa na posição zero
                    print('\n\033[1;96m----------------------------------------------\033[0;0m')
                    print('\033[1;96m Histórico por posição \033[0;0m')
                    print('\033[1;96m----------------------------------------------\033[0;0m')
                    print('\033[1;34mOperação ' + str(posicao_escolhida) +': \033[0;0m' +log_hist[posicao_hist])
                    print('\033[1;96m\n----------------------------------------------\033[0;0m')
                    print('\033[1;96m Fim Histórico \033[0;0m')
                    print('\033[1;96m----------------------------------------------\033[0;0m')
                else:
                    print('\n\033[7;33m'+'Posição não existe'+'\033[0;0m')
            elif operacao_hist != '1' or '2':
                print('\n\033[7;33m'+'Opção inválida!!! Voltando ao menu inicial...'+'\033[0;0m')
                continue

            refazerOper()

        if operacao != '5':
            print('\n\033[1;32m'+'Resultado: '+'\033[0;0m' + str(ResultCalc.n1) + ' ' + str(temp) + ' ' + str(ResultCalc.n2) + ' = ' + str(result))
            log_hist.append('\033[0;0m' + str(ResultCalc.n1) + ' ' + str(temp) + ' ' + str(ResultCalc.n2) + ' = ' + str(result))

            refazerOper()

    except:
        print('\n\033[7;31m'+'------ FALHA NA OPERAÇÃO ------\033[0;0m')
        refazerOper()
