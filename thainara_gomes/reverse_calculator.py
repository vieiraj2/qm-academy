from thainara_gomes.calculator import Calculator


class ReverseCalculator(Calculator):

    def __init__(self, num1, num2):
        self.num1 = num2
        self.num2 = num2
        super().__init__(num1, num2)

    def sum(self, num1, num2):
        return super().sub(num1, num2)

    def sub(self, num1, num2):
        return super().sum(num1, num2)

    def multi(self, num1, num2):
        return super().div(num1, num2)

    def div(self, num1, num2):
        return super().mult(num1, num2)
