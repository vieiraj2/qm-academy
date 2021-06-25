# Challenge 5 - Ana & Mari

class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def sum(self):
        sum = self.number1 + self.number2
        print(f'The sum is: {self.number1} + {self.number2} = {sum}')
        return sum

    def sub(self):
        sub = self.number1 - self.number2
        print(f'The subtraction is: {self.number1} - {self.number2} = {sub}')
        return sub

    def multi(self):
        multi = self.number1 * self.number2
        print(f'The multiplication is: {self.number1} - {self.number2} = {multi}')
        return multi

    def div(self):
        div = self.number1 / self.number2
        print(f'The division is: {self.number1} - {self.number2} = {div}')
        return div

