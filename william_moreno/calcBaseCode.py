from calculator_concat_sum import *
import os

cal_history = []
option = None


def clear():
    os.environ["TERM"] = "linux"
    os.system("clear")


def history(op_result):
    cal_history.append(op_result)


def is_float(a):
    try:
        float(a)
        return True
    except ValueError:
        return False


def is_int(a):
    try:
        int(a)
        return True
    except ValueError:
        return False


def choose_operation(choose_option, a, b):
    calculator = CalculatorConcatSum(a, b)
    if choose_option == 'a' or choose_option == 'soma' or choose_option == '1':
        op_result = calculator.sum()
        history(op_result)
    elif choose_option == 'b' or choose_option == 'subtração' or choose_option == '2':
        op_result = calculator.sub()
        history(op_result)
    elif choose_option == 'c' or choose_option == 'multiplicação' or choose_option == '3':
        op_result = calculator.mult()
        history(op_result)
    elif choose_option == 'd' or choose_option == 'divisão' or choose_option == '4':
        op_result = calculator.div()
        if op_result:
            history(op_result)


def choose_operation_is_valid(choose_option):
    if choose_option == 'a' or choose_option == 'soma' or choose_option == '1':
        return True
    elif choose_option == 'b' or choose_option == 'subtração' or choose_option == '2':
        return True
    elif choose_option == 'c' or choose_option == 'multiplicação' or choose_option == '3':
        return True
    elif choose_option == 'd' or choose_option == 'divisão' or choose_option == '4':
        return True
    elif choose_option == 'e' or choose_option == 'consultar' or choose_option == 'historico' or choose_option == '5':
        return True
    else:
        return False


def input_value(msg):
    while True:
        value = input(msg)
        if is_int(value):
            value = int(value)
            break
        elif is_float(value):
            value = float(value)
            break
        else:
            print("\033[0;31mO valor digitado não é um valor válido, digite novamente!\033[m")
    return value


def leia_str(msg):
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
    operation = leia_str("Digite a opção desejada: ")

    while not choose_operation_is_valid(operation):
        operation = leia_str("\033[0;31mVocê digitou uma opção inválida. Digite novamente a opção desejada: \033[m")

    if not (operation == 'e' or operation == 'consultar' or operation == 'historico' or operation == '5'):
        value1 = input_value("Digite o primeiro valor: ")
        value2 = input_value("Digite o segundo valor: ")

        choose_operation(operation, value1, value2)
    elif operation == 'e' or operation == 'consultar' or operation == 'historico' or operation == '5':
        print("\nDeseja verificar o histórico total ou parcial?")
        print("\n1. Histórico total")
        print("2. Histórico parcial\n")
        operation_history = input("Por favor, digite a opção desejada: ")

        if operation_history == '1' or operation_history == 'total':
            count = 1
            if len(cal_history) <= 0 or type(cal_history) is None:
                print("\n\033[0;31mVocê ainda não possui histórico de operações \033[m")
            else:
                for i in cal_history:
                    print(f"Operação #{count}: {i[0]} {i[1]} {i[2]} {i[3]} {i[4]}")
                    count += 1
        elif operation_history == '2' or operation_history == 'parcial':
            count = 1
            if len(cal_history) <= 0:
                print("\n\033[0;31mVocê ainda não possui histórico de operações \033[m")
            else:
                print("\nVeja abaixo as posições disponíveis no histórico: ")
                for i in cal_history:
                    print(f"Operação #{count}")
                    count += 1

                operation_history_parcial = input("\nPor favor, digite qual posição deseja consultar: ")

                while True:
                    if int(operation_history_parcial) <= 0 or int(operation_history_parcial) > (count - 1):
                        print("\n\033[0;31mEssa posição não existe no nosso histórico. "
                              "Por favor verifique as opções válidas a seguir\033[m")
                        count2 = 1
                        for i in cal_history:
                            print(f"Operação #{count2}")
                            count2 += 1
                        operation_history_parcial = input("\nPor favor, digite qual posição deseja consultar: ")
                    else:
                        count3 = 1
                        for i in cal_history:
                            if count3 == int(operation_history_parcial):
                                print(f"Operação #{count3}: {i[0]} {i[1]} {i[2]} {i[3]} {i[4]}")
                            count3 += 1
                        break

    print("\nO que deseja fazer agora?")
    print("1- Fazer outra operação \n2- Encerrar o programa\n")
    option = input()
    clear()
