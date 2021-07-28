from calculator import Calculator


class ReverseCalculator(Calculator):

    def addition(self):
        return Calculator.sub(self)

    def sub(self):
        return Calculator.addition(self)

    def multiply(self):
        return Calculator.divide(self)

    def divide(self):
        return Calculator.multiply(self)
