# !/usr/bin/env python3
# File: calculator_concat_sum.py (here a new class defined which extends Calculator class and
# redefines the method "soma" (sum). Instead of summing two numbers, the method will concatenate these numbers as strings

from calculator import *

class CalculatorConcatSum(Calculator):
    def __init__(self, oper1, oper2):
        # Just initializing the attributes
        self.oper1 = oper1
        self.oper2 = oper2
    def soma(self):
        resultado = str(self.oper1) + str(self.oper2)
        return (resultado)