import os

calHistory = []
option = None

def clear():
    os.environ["TERM"] = "linux"
    os.system("clear")


def sum_calc(a, b):
    print(f"O resultado da soma é {a + b}\n")
    opResult = [a, "+", b, "=", (a + b)]
    history(opResult)


def subtraction_calc(a, b):
    print(f"O resultado da subtração é {a - b}\n")
    opResult = [a, "-", b, "=", (a - b)]
    history(opResult)

def multiplication_calc(a, b):
    print(f"O resultado da multiplicação é {a * b}\n")
    opResult = [a, "*", b, "=", (a * b)]
    history(opResult)

def division_calc(a, b):
    print(f"O resultado da divisão é {a / b}\n")
    opResult = [a, "/", b, "=", (a / b)]
    history(opResult)

def history(opResult):
    calHistory.append(opResult)


def chooseOperation(chooseOption, a, b):
    if chooseOption == 'a' or chooseOption == 'soma' or chooseOption == '1':
        sum_calc(a, b)
    elif chooseOption == 'b' or chooseOption == 'subtração' or chooseOption == '2':
        subtraction_calc(a, b)
    elif chooseOption == 'c' or chooseOption == 'multiplicação' or chooseOption == '3':
        multiplication_calc(a, b)
    elif chooseOption == 'd' or chooseOption == 'divisão' or chooseOption == '4':
        division_calc(a, b)

def chooseOperationIsValid(chooseOption):
    if chooseOption == 'a' or chooseOption == 'soma' or chooseOption == '1':
        return True
    elif chooseOption == 'b' or chooseOption == 'subtração' or chooseOption == '2':
        return True
    elif chooseOption == 'c' or chooseOption == 'multiplicação' or chooseOption == '3':
        return True
    elif chooseOption == 'd' or chooseOption == 'divisão' or chooseOption == '4':
        return True
    elif chooseOption == 'e' or chooseOption == 'consultar' or chooseOption == 'historico' or chooseOption == '5':
        return True
    else:
        return False



def inputValue(msg,operation, inputNumber):
    while True:
        value = input(msg)
        if value.isnumeric():
            if (operation == 'd' or operation == 'divisão' or operation == '4') and (inputNumber == 2):
                value = float(value)
                if value == 0:
                    print("\033[0;31mNão é possível realizar uma divisão por zero, digite outro valor\033[m")
                else:
                    break
            else:
                value = float(value)
                break
        else:
            print("\033[0;31mO valor digitado não é um valor válido, digite novamente!\033[m")
    return value


def leiaStr (msg):

    while True:
        value = input(msg)
        if len(value) == 0:
            print("\033[0;31mErro opção inválida, digite novamente!\033[m")
        else:
            break
    return value


while option != '2':
    print("Seja bem vindo a Calculadora.py")
    print("a. Soma")
    print("b. Subtração")
    print("c. Multiplicação")
    print("d. Divisão")
    print("e. Consultar o histórico")
    operation = leiaStr("Digite a opção desejada: ")

    while not chooseOperationIsValid(operation):
        operation = leiaStr("\033[0;31mVocê digitou uma opção inválida. Digite novamente a opção desejada: \033[m")

    if not (operation == 'e' or operation == 'consultar' or operation == 'historico' or operation == '5'):
        value1 = inputValue("Digite o primeiro valor: ", operation, 1)
        value2 = inputValue("Digite o segundo valor: ", operation, 2)

        chooseOperation(operation, value1, value2)
    elif operation == 'e' or operation == 'consultar' or operation == 'historico' or operation == '5':
        print("\nDeseja verificar o histórico total ou parcial?")
        print("\n1. Histórico total")
        print("2. Histórico parcial\n")
        operationHistory = input("Por favor, digite a opção desejada: ")

        if operationHistory == '1' or operationHistory == 'total':
            count = 1
            if len(calHistory) <= 0:
                print("\n\033[0;31mVocê ainda não possui histórico de operações \033[m")
            else:
                for i in calHistory:
                    print(f"Operação #{count}: {i[0]} {i[1]} {i[2]} {i[3]} {i[4]}")
                    count += 1
        elif operationHistory == '2' or operationHistory == 'parcial':
            count = 1
            if len(calHistory) <= 0:
                print("\n\033[0;31mVocê ainda não possui histórico de operações \033[m")
            else:
                print("\nVeja abaixo as posições disponíveis no histórico: ")
                for i in calHistory:
                    print(f"Operação #{count}")
                    count += 1

                operationHistoryParcial = input("\nPor favor, digite qual posição deseja consultar: ")

                while True:
                    if int(operationHistoryParcial) <= 0 or int(operationHistoryParcial) > (count - 1):
                        print("\n\033[0;31mEssa posição não existe no nosso histórico. Por favor verifique as opções válidas a seguir. \033[m")
                        count2 = 1
                        for i in calHistory:
                            print(f"Operação #{count2}")
                            count2 += 1
                        operationHistoryParcial = input("\nPor favor, digite qual posição deseja consultar: ")
                    else:
                        count3 = 1
                        for i in calHistory:
                            if count3 == int(operationHistoryParcial):
                                print(f"Operação #{count3}: {i[0]} {i[1]} {i[2]} {i[3]} {i[4]}")
                            count3 += 1
                        break


    print("\nO que deseja fazer agora?")
    print("1- Fazer outra operação \n2- Encerrar o programa\n")
    option = input()
    clear()