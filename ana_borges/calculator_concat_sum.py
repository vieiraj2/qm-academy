# Challenge 5 - Ana & Mari

from calculator import Calculator


class CalculatorConcatSum(Calculator):
    def sum(self):
        int_n1 = int(self.number1)
        int_n2 = int(self.number2)
        concat = float(str(int_n1) + str(int_n2))
        print(f'The concatenation is: {self.number1} concat {self.number2} = {concat}')
        return concat
