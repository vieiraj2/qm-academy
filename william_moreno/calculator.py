class Calculator:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def sum(self):
        print(f"O resultado da soma é {self._a + self._b}\n")
        op_result = [self._a, "+", self._b, "=", (self._a + self._b)]
        return op_result

    def sub(self):
        print(f"O resultado da subtração é {self._a - self._b}\n")
        op_result = [self._a, "-", self._b, "=", (self._a - self._b)]
        return op_result

    def mult(self):
        print(f"O resultado da multiplicação é {self._a * self._b}\n")
        op_result = [self._a, "*", self._b, "=", (self._a * self._b)]
        return op_result

    def div(self):
        try:
            print(f"O resultado da divisão é {self._a / self._b}\n")
            op_result = [self._a, "/", self._b, "=", (self._a / self._b)]
            return op_result
        except ZeroDivisionError:
            print("\033[0;31mNão é possível realizar uma divisão por zero\033[m")
            return False
