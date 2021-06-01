import os


cal_history = []
option = None


def clear():
    os.environ["TERM"] = "linux"
    os.system("clear")


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


def sum_calc(a, b):
    print(f"O resultado da soma é {a + b}\n")
    op_result = [a, "+", b, "=", (a + b)]
    history(op_result)


def subtraction_calc(a, b):
    print(f"O resultado da subtração é {a - b}\n")
    op_result = [a, "-", b, "=", (a - b)]
    history(op_result)


def multiplication_calc(a, b):
    print(f"O resultado da multiplicação é {a * b}\n")
    op_result = [a, "*", b, "=", (a * b)]
    history(op_result)


def division_calc(a, b):
    print(f"O resultado da divisão é {a / b}\n")
    op_result = [a, "/", b, "=", (a / b)]
    history(op_result)


def history(op_result):
    cal_history.append(op_result)


def choose_operation(choose_option, a, b):
    if choose_option == 'a' or choose_option == 'soma' or choose_option == '1':
        sum_calc(a, b)
    elif choose_option == 'b' or choose_option == 'subtração' or choose_option == '2':
        subtraction_calc(a, b)
    elif choose_option == 'c' or choose_option == 'multiplicação' or choose_option == '3':
        multiplication_calc(a, b)
    elif choose_option == 'd' or choose_option == 'divisão' or choose_option == '4':
        division_calc(a, b)


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


def input_value(msg, choosed_operation, input_number):
    while True:
        value = input(msg)

        if (choosed_operation == 'd' or choosed_operation == 'divisão' or choosed_operation == '4') \
                and (input_number == 2):
            if is_int(value):
                value = int(value)
                if value == 0:
                    print("\033[0;31mNão é possível realizar uma divisão por zero, digite outro valor\033[m")
                else:
                    return value
            elif is_float(value):
                value = float(value)
                if value == 0.0:
                    print("\033[0;31mNão é possível realizar uma divisão por zero, digite outro valor\033[m")
                else:
                    return value

            else:
                print("\033[0;31mO valor digitado não é um valor válido, digite novamente!\033[m")

        else:

            if is_int(value):
                value = int(value)
                return value

            elif is_float(value):
                value = float(value)
                return value

            else:
                print("\033[0;31mO valor digitado não é um valor válido, digite novamente!\033[m")


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
        value1 = input_value("Digite o primeiro valor: ", operation, 1)
        value2 = input_value("Digite o segundo valor: ", operation, 2)

        choose_operation(operation, value1, value2)
    elif operation == 'e' or operation == 'consultar' or operation == 'historico' or operation == '5':
        print("\nDeseja verificar o histórico total ou parcial?")
        print("\n1. Histórico total")
        print("2. Histórico parcial\n")
        operation_history = input("Por favor, digite a opção desejada: ")

        if operation_history == '1' or operation_history == 'total':
            count = 1
            if len(cal_history) <= 0:
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
                              "Por favor verifique as opções válidas a seguir. \033[m")
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
