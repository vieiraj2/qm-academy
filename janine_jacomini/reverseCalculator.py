from janine_jacomini.calculator import Calculator


class ReverseCalculator(Calculator):
    def sum(self):
        soma = self.n1 - self.n2
        return soma

    def sub(self):
        subtracao = self.n1 + self.n2
        return subtracao

    def mult(self):
        multiplicacao = self.n1 / self.n2
        return multiplicacao

    def div(self):
        divisao = self.n1 * self.n2
        return divisao
