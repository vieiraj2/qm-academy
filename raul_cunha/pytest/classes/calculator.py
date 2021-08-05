class Calculator:
    def __init__(self, oper1, oper2):
        # Just initializing the attributes
        self.oper1 = oper1
        self.oper2 = oper2

    def soma(self):
        return self.oper1 + self.oper2

    def subtrai(self):
        return self.oper1 - self.oper2

    def multiplica(self):
        return self.oper1 * self.oper2

    def divide(self):
        try:
            return self.oper1 / self.oper2
        except ZeroDivisionError:
            print('It does not exist a division by zero!')
            print('\n')
