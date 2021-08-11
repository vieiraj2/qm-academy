from calculator import Calculator as BaseCalc


class ReverseCalc(BaseCalc):
    def soma(self, value1, value2):
        return BaseCalc().sub(value1, value2)

    def sub(self, value1, value2):
        return BaseCalc().soma(value1, value2)

    def mult(self, value1, value2):
        return BaseCalc().div(value1, value2)

    def div(self, value1, value2):
        return BaseCalc().mult(value1, value2)


# su = ReverseCalc().soma(10, 10)
# print(su)
# sub = ReverseCalc().sub(10, 10)
# print(sub)
# mult = ReverseCalc().mult(10, 10)
# print(mult)
# div = ReverseCalc().div(10, 10)
# print(div)
