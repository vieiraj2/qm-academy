class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def sum(self):
        sum = self.value1 + self.value2
        print(f'Your result is: {self.value1} + {self.value2} = {sum}')
        return sum

    def sub(self):
        sub = self.value1 - self.value2
        print(f'Your result is: {self.value1} - {self.value2} = {sub}')
        return sub

    def multi(self):
        multi = self.value1 * self.value2
        print(f'Your result is: {self.value1} - {self.value2} = {multi}')
        return multi

    def div(self):
        div = self.value1 / self.value2
        print(f'Your result is: {self.value1} - {self.value2} = {div}')
        return div
