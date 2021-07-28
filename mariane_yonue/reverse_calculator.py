from .calculator import Calculator


class ReverseCalculator(Calculator):
    def sum(self, number1, number2):
        return Calculator.sub(self, number1, number2)

    def sub(self, number1, number2):
        return Calculator.sum(self, number1, number2)

    def mult(self, number1, number2):
        return Calculator.div(self, number1, number2)

    def div(self, number1, number2):
        return Calculator.multi(self, number1, number2)
