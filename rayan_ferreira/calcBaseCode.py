import os

option = None

def clear():
    os.environ["TERM"] = "linux"
    os.system("clear")


def sum_calc(a, b):
    print(f"O resultado da soma é {a + b}\n")


def subtraction_calc(a, b):
    print(f"O resultado da subtração é {a - b}\n")


def multiplication_calc(a, b):
    print(f"O resultado da multiplicação é {a * b}\n")


def division_calc(a, b):
    print(f"O resultado da divisão é {a / b}\n")


def chooseOperation(chooseOption, a, b):
    if chooseOption == 'a' or chooseOption == 'soma' or chooseOption == '1':
        sum_calc(a, b)
    elif chooseOption == 'b' or chooseOption == 'subtração' or chooseOption == '2':
        subtraction_calc(a, b)
    elif chooseOption == 'c' or chooseOption == 'multiplicação' or chooseOption == '3':
        multiplication_calc(a, b)
    elif chooseOption == 'd' or chooseOption == 'divisão' or chooseOption == '4':
        division_calc(a, b)


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
    operation = leiaStr("Digite a opção desejada: ")

    value1 = inputValue("Digite o primeiro valor: ", operation, 1)
    value2 = inputValue("Digite o segundo valor: ", operation, 2)

    chooseOperation(operation, value1, value2)

    print("O que deseja fazer agora?")
    print("1- Fazer outra operação \n2- Encerrar o programa\n")
    option = input()
    clear()
