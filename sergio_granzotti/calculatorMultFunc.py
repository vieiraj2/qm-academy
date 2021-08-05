from calculator import Calculator


class calculatorMultFunc(Calculator):
    # Soma intervalo
    def item_1(self, n1, n2):
        sunInterval = 0
        for x in range(n1 + 1, n2):
            sunInterval = sunInterval + x
        return sunInterval

    # Fibonacci
    def item_2(self, n1):
        proximo = 0
        anterior = 0
        index = 0
        while n1 > index:
            index = index + 1
            proximo = proximo + anterior
            anterior = proximo - anterior
            if proximo == 0:
                proximo = proximo + 1
        return proximo

    # Print odd
    def item_3(self, n1):
        lista = []
        index = 0
        while index < len(n1):
            if (index % 2) == 0:
                print(n1[index], end=' ')
                lista.append(n1[index])
            index = index + 1
            print(lista)
        return lista

    # Soma_Calculator
    def sum(self):
        soma = self.n1 + self.n2
        return soma

    # subtracao_Calculator
    def sub(self):
        subtracao = self.n1 - self.n2
        return subtracao

    # Multiplicação_Calculator
    def mult(self):
        multiplicacao = self.n1 * self.n2
        return multiplicacao

    # Divisao_Calculator
    def div(self):
        divisao = self.n1 / self.n2
        return divisao
