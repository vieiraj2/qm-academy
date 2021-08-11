import os
import sys


class Calculator:

    def clear(self):
        os.environ['TERM'] = 'linux'
        os.system('clear')

    def sair(self):
        sys.exit()

    def soma(self, value1, value2):
        return value1 + value2

    def sub(self, value1, value2):
        return value1 - value2

    def mult(self, value1, value2):
        return value1 * value2

    def div(self, value1, value2):
        return value1 / value2
