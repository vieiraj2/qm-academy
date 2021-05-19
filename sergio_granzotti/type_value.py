#Challange 2 - Types and values
#Usando eval() pois no python3 a função input retorna sempre string

try:
    x = eval(input("Por favor, digite qualquer valor: "))
    print(type(x))
except:
    print('string')

try:
    y = eval(input("Digite um valor: "))
    print(type(y))
    
except:
    print('string')