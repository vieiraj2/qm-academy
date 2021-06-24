from calculator import Calculator


class CalculatorConcatSum(Calculator):
    def sum(self, num1, num2):
        resul = str(num1) + str(num2)
        print('Resultado {}, {} concatenação {}'.format(num1, num2, resul))
        return resul
