from .calculator import Calculator


class CalculatorMultFunc(Calculator):

    def interval_sum(self, n1, n2):
        total_sum = 0
        start = Calculator.sum(self, n1, 1)
        for i in range(start, n2):
            total_sum = Calculator.sum(self, i, total_sum)
        return total_sum

    def fibonacci_position(self, position):
        previous_number = 1
        next_number = 1
        end = Calculator.sum(self, position, 1)

        if position == 1 or position == 2:
            return 1

        if position <= 0:
            raise Exception('Position provided is not positive integer')

        for i in range(3, end):
            current = Calculator.sum(self, previous_number, next_number)
            previous_number = next_number
            next_number = current
        return current

    def print_odd_strings(self, strings):
        list = []
        if not strings:
            raise Exception('There were no strings in the list')
        for i in range(0, len(strings), 2):
            print(strings[i])
            list.append(strings[i])

        return list

    def sum(self, number1, number2):
        return Calculator.sum(self, number1, number2)

    def sub(self, number1, number2):
        return Calculator.sub(self, number1, number2)

    def div(self, number1, number2):
        return Calculator.div(self, number1, number2)

    def multi(self, number1, number2):
        return Calculator.multi(self, number1, number2)
