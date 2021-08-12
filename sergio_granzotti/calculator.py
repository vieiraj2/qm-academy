# Challenge 5 - Team 4 - Calculator


class Calculator:
    def __init__(self, n1, n2):  # init: construtor 'obriga' q use sempre os dois numeros
        self.n1 = n1
        self.n2 = n2

    def sum(self):
        soma = self.n1 + self.n2
        return soma

    def sub(self):
        subtracao = self.n1 - self.n2
        return subtracao

    def mult(self):
        multiplicacao = self.n1 * self.n2
        return multiplicacao

    def div(self):
        try:
            divisao = self.n1 / self.n2
            return divisao
        except ZeroDivisionError:
            print('FALHA NA OPERAÇÃO!!! Não é possivel realizar divisão por zero!!!')  # divisao por zero
