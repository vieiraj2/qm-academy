#Challenge 2
#Usando eval() pois no python3 a função input retorna sempre string

try:
    x = eval(input("Digite um valor: "))
    print(type(x))
    
except:
    print('string')


try:
    y = eval(input("Digite um valor: "))
    print(type(y))
    
except:
    print('string')
