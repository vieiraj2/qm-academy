def type_values(par1, par2):
    try:
        print('A primeira entrada foi ', type(eval(par1)))
    except:
        if par1 != '':
            print('A primeira entrada foi STRING')
        else:
            print('A primeira entrada foi NULL')
    try:
        print('A segunda entrada foi ', type(eval(par2)))
    except:
        if par2 != '':
            print('A segunda entrada foi STRING')
        else:
            print('A segunda entrada foi NULL')

continua = True
while continua:
#    os.system('clear')
    par3 = input('Entre com o PRIMEIRO parâmetro para ser verificado seu tipo, e após tecle <ENTER>: ')
    par4 = input('Entre com o SEGUNDO parâmetro para ser verificado seu tipo, e após tecle <ENTER>: ')
    type_values(par3, par4)
    resposta = input('Repetir? S/N : ')
    if resposta != "S" and resposta != "s":
        continua = False