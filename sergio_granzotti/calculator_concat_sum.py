#Challenge 5 - Team 4 - Calculator_concat_sum

from calculator import Calculator

class CalculatorConcatSum(Calculator):
    def sum(self):
        self.n1 = float(input('Digite o primeiro número: '))
        self.n2 = float(input('Digite o segundo número: '))
        concat = str(self.n1) + str(self.n2)
        return concat