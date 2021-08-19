from sergio_granzotti.calculator import Calculator


class ReverseCalculator(Calculator):
    def sum(self):
        return super().sub()

    def sub(self):
        return super().sum()

    def mult(self):
        return super().div()

    def div(self):
        return super().mult()
