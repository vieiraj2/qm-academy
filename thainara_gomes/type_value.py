# Inicio
def type_values(num1, num2):
    try:
        print('A primeira entrada foi ', type(eval(num1)))
    except:
        if num1 != '':
            print('A primeira entrada foi STRING')
        else:
            print('A primeira entrada foi NULL')
    try:
        print('A segunda entrada foi ', type(eval(num2)))
    except:
        if num2 != '':
            print('A segunda entrada foi STRING')
        else:
            print('A segunda entrada foi NULL')


continua = True
while continua:
    num3 = input('Digite o primeiro parâmetro: ')
    num4 = input('Digite o segundo parâmetro: ')
    type_values(num3, num4)
    resposta = input('Repetir? S/N : ')
    if resposta != "S" and resposta != "s":
        continua = False
