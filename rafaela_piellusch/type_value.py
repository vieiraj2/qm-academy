def funcao():
    tipos = (1, 1.2, True, 'Rafaela',[1,2,3,4], {'Rafa': 20}, None, (1, 2, 4, 5) )
    for c in tipos:
        print('O tipo de {} é {}'.format(c, type(c)))


funcao()
