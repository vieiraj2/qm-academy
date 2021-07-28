# Challenge 5 - Ana & Mari

class Calculator:
    def sum(self, number1, number2):
        sum = number1 + number2
        print(f'The sum is: {number1} + {number2} = {sum}')
        return sum

    def sub(self, number1, number2):
        sub = number1 - number2
        print(f'The subtraction is: {number1} - {number2} = {sub}')
        return sub

    def multi(self, number1, number2):
        multi = number1 * number2
        print(f'The multiplication is: {number1} - {number2} = {multi}')
        return multi

    def div(self, number1, number2):
        div = number1 / number2
        print(f'The division is: {number1} - {number2} = {div}')
        return div
