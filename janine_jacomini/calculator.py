#Challenge 5 - Team 4 - Calculator

class Calculator:
    def __init__(self, n1, n2): #init: construtor 'obriga' q use sempre os dois numeros
        self.n1 = n1
        self.n2 = n2

    def sum(self):
        self.n1 = float(input('Digite o primeiro número: '))
        self.n2 = float(input('Digite o segundo número: '))
        soma = self.n1 + self.n2
        return soma

    def sub(self):
        self.n1 = float(input('Digite o primeiro número: '))
        self.n2 = float(input('Digite o segundo número: '))
        subtracao = self.n1 - self.n2
        return subtracao

    def mult(self):
        self.n1 = float(input('Digite o primeiro número: '))
        self.n2 = float(input('Digite o segundo número: '))
        multiplicacao = self.n1 * self.n2
        return multiplicacao

    def div(self):
        try:
            self.n1 = float(input('Digite o primeiro número: '))
            self.n2 = float(input('Digite o segundo número: '))
            divisao = self.n1 / self.n2
            return divisao
        except:
            print('FALHA NA OPERAÇÃO!!! Não é possivel realizar divisão por zero!!!') #divisao por zero







