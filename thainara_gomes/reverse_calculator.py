from thainara_gomes.calculator import Calculator


class ReverseCalculator(Calculator):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        super().__init__(num1, num2)

    def sum(self):
        return super().sub()

    def sub(self):
        return super().sum()

    def multi(self):
        return super().div()

    def div(self):
        return super().mult()
