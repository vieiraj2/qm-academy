# Challenge 5 - Team 4 - Calculator_concat_sum

from calculator import Calculator


class CalculatorConcatSum(Calculator):
    def sum(self):
        concat = str(self.n1) + str(self.n2)
        return concat
