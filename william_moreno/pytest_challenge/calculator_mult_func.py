from william_moreno.pytest_challenge.calculator import Calculator as BaseCalc

concatenated_list_result = []


def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    # initialize parameters
    if numargs < 1:
        raise TypeError(f'Expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        # desempacotamento (python). Se a lista possui apenas 2 posições, a primeira variável
        # será atribuída a primeira posição da lista e a segunda variável
        # será atribuída a segunda posição da lista. O mesmo ocorre quando 'numargs == 3'.
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'Expected at most 3 arguments, got {numargs}')

    # generator
    i = start + 1
    while i <= stop - 1:
        yield i
        i += step


class CalculatorMultFunc(BaseCalc):

    def concateneted_sum(self, n1, n2):
        result = ''
        concatenated_list = []

        for i in inclusive_range(n1, n2):
            concatenated_list.append(str(i))

        for i in range(len(concatenated_list)):
            result = result + concatenated_list[i]

        # print(result)
        # print(concatenated_list)
        return result

    def fibonacci(self, n):
        lista = []
        fibonacci = 0
        last = 1
        antepenultimate = 0

        i = 0
        while i < n:
            i += 1
            antepenultimate = last
            last = fibonacci
            fibonacci = antepenultimate + last
            lista.append(fibonacci)

        return lista[n - 1]


# def user_menu():
#     # for i in inclusive_range(1, 10, 1):
#     #     print (i, end = ' ')
#     # print()
#     calc = CalculatorMultFunc()
#     option = None
#
#     while option != 'sair'.lower():
#         print("1. Concatenated SUM")
#         print("2. Fibonnaci number by position")
#
#         operation = input("Por favor digite a opção desejada: ")
#
#         if operation == '1':
#             value1 = int(input("Por favor, digite o primeiro valor: "))
#             value2 = int(input("Por favor, digite o segundo valor: "))
#
#             calc.concateneted_sum(value1, value2)
#
#         if operation == '2':
#             fibo_position = int(input("Digite a posição que deseja consultar dentro da sequência de fibonacci: "))
#             fibo_list = calc.fibonacci(fibo_position)
#             print(fibo_list)
#             print(f"Output: {lista[fibo_position - 1]}\n")
#
#         print("\nO que deseja fazer agora?")
#         print("1- Fazer outra operação \n2- Encerrar o programa\n")
#         option = input()
#
#         if option == '2':
#             calc.sair()
#         else:
#             calc.clear()
#
#     # a = CalculatorMultFunc()
#     # a.concateneted_sum(1, 10)


# if __name__ == '__main__':
#     user_menu()
