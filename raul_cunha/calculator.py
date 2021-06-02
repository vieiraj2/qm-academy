#!/usr/bin/env python3
# New file: calculator.py (instead of calc.py)
# Program based on first Calculator version which considered integer numbers - Addition, Subtraction, Multiplication a
# nd Division
# IMPROVEMENTS - History of operations
# This actual version contains a refactoring of code, including classes and methods instead
# And also is considering the new file "calculator_concat_sum.py" which has a new implementation (Concat) for the
# method "soma" (sum).

from calculator_concat_sum import *


class Calculator:
    def __init__(self, oper1, oper2):
        # Just initializing the attributes
        self.oper1 = oper1
        self.oper2 = oper2

    def soma(self):
        return self.oper1 + self.oper2

    def subtrai(self):
        return self.oper1 - self.oper2

    def multiplica(self):
        return self.oper1 * self.oper2

    def divide(self):
        try:
            return self.oper1 / self.oper2
        except ZeroDivisionError:
            print('It does not exist a division by zero!')
            print('\n')


def main():
    continua = True     # variavel de controle do loop principal WHILE
    historic = []      # Lista p/ armazenamento de informações de operações para Histórico
    while continua:

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
        if operacao == '6':
            continua = False
            continue
        elif operacao == '5':
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
                for j in range(len(historic)):
                    print(historic[j])
                    print('\n')
            elif option_hist == '2':
                try:
                    option_oper = int(input('Type which operation would you like to search: '))
                except Exception as err:
                    print(err)
                    print('Invalid input(s)!')
                    print('\n')
                    continue
                if option_oper != 0:
                    print(historic[option_oper - 1])
                    print('\n')
                else:
                    print('Invalid input(s)!')
            else:
                print('\n')
                continue

        elif operacao == '1':
            print('* Addition *')
            try:
                oper1 = float(input('Input the first operator, and after press <ENTER>: '))
                oper2 = float(input('Input the second operator, and after press <ENTER>: '))
            except Exception:
                print('Invalid input(s)!')
                print('\n')
                continue

            # Constrói uma instância do objeto "Calculator", com os parâmetros inputados pelo usuário
            objcalc = CalculatorConcatSum(oper1, oper2)

            # Executa o método "soma", tendo como entrada os valores inputados pelo usuário, e utilizados no
            # instanciamento do objeto
            resultado = objcalc.soma()

            # Imprime o resultado da operação
            print('Result of operation: ', resultado)

            # GUARDA NO HISTORICO (LISTA)
            content = (oper1, " + ", oper2, ' = ', resultado)
            historic.append(content)
            print('\n')

        elif operacao == '2':
            print('* Subtraction *')
            try:
                oper1 = int(input('Input the first operator, and after press <ENTER>: '))
                oper2 = int(input('Input the second operator, and after press <ENTER>: '))
            except Exception:
                print('Invalid input(s)!')
                print('\n')
                continue

            # Constrói uma instância do objeto "Calculator", com os parâmetros inputados pelo usuário
            objcalc = CalculatorConcatSum(oper1, oper2)

            # Executa o método "subtrai", tendo como entrada os valores inputados pelo usuário, e utilizados no
            # instanciamento do objeto
            resultado = objcalc.subtrai()

            # Imprime o resultado da operação
            print('Result of operation: ', resultado)

            # GUARDA NO HISTORICO (LISTA)
            content = (oper1, " - ", oper2, ' = ', resultado)
            historic.append(content)
            print('\n')

        elif operacao == '3':
            print('* Multiplication *')
            try:
                oper1 = int(input('Input the first operator, and after press <ENTER>: '))
                oper2 = int(input('Input the second operator, and after press <ENTER>: '))
            except Exception:
                print('Invalid input(s)!')
                print('\n')
                continue

            # Constrói uma instância do objeto "Calculator", com os parâmetros inputados pelo usuário
            objcalc = CalculatorConcatSum(oper1, oper2)

            # Executa o método "multiplica", tendo como entrada os valores inputados pelo usuário, e utilizados no
            # instanciamento do objeto
            resultado = objcalc.multiplica()

            # Imprime o resultado da operação
            print('Result of operation: ', resultado)

            # GUARDA NO HISTORICO (LISTA)
            content = (oper1, " * ", oper2, ' = ', resultado)
            historic.append(content)
            print('\n')

        elif operacao == '4':
            print('* Division *')
            try:
                oper1 = int(input('Input the first operator, and after press <ENTER>: '))
                oper2 = int(input('Input the second operator, and after press <ENTER>: '))
            except Exception:
                print('Invalid input(s)!')
                print('\n')
                continue

            # Constrói uma instância do objeto "Calculator", com os parâmetros inputados pelo usuário
            objcalc = CalculatorConcatSum(oper1, oper2)

            # Executa o método "divide", tendo como entrada os valores inputados pelo usuário, e utilizados no
            # instanciamento do objeto
            resultado = objcalc.divide()

            if resultado is not None:
                # Imprime o resultado da operação
                print('Result of operation: ', resultado)
                # GUARDA NO HISTORICO (LISTA)
                content = (oper1, " / ", oper2, ' = ', resultado)
                historic.append(content)
                print('\n')
            else:
                continue
        else:
            print('Invalid option!')

        print('\n')
        resposta = input('Repeat CALCULATOR? Y/N : ')
        if resposta != "Y" and resposta != "y":
            continua = False
        print('\n')


if __name__ == '__main__':
    main()
