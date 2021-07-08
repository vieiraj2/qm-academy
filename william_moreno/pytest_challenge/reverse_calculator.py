from william_moreno.pytest_challenge.calculator import Calculator as BaseCalc


class ReverseCalc(BaseCalc):
    def soma(self, value1, value2):
        return value1 - value2

    def sub(self, value1, value2):
        return value1 + value2

    def mult(self, value1, value2):
        return value1 / value2

    def div(self, value1, value2):
        return value1 * value2
