# !/usr/bin/env python3

from raul_cunha.pytest.classes.calculator import Calculator


class ReverseCalculator(Calculator):

    def __init__(self, oper1, oper2):
        self.oper1 = oper1
        self.oper2 = oper2
        super().__init__(oper1, oper2)

    def soma(self):
        return super().subtrai()

    def subtrai(self):
        return super().soma()

    def multiplica(self):
        return super().divide()

    def divide(self):
        return super().multiplica()
