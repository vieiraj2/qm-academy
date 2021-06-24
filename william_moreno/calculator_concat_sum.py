from calculator import *


class CalculatorConcatSum(Calculator):

    def sum(self):
        print(f"O resultado da soma concatenada é {str(self._a) + str(self._b)}\n")
        op_result = [self._a, "+", self._b, "=", (str(self._a) + str(self._b))]
        return op_result
