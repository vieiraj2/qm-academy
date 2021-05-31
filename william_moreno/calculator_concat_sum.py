from calculator import *


class CalculatorConcatSum(Calculator):

    def sum(self):
        print(f"O resultado da soma concatenada é {str(self._a) + str(self._b)}\n")
        opResult = [self._a, "+", self._b, "=", (str(self._a) + str(self._b))]
        return opResult