from calculator import Calculator


class ReverseCalculator(Calculator):

    def addition(self):
        return self.a - self.b

    def sub(self):
        return self.a + self.b

    def multiply(self):
        return self.a / self.b

    def divide(self):
        return self.a * self.b
