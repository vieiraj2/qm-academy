from .calculator import Calculator


class CalculatorMultFunc(Calculator):
    def interval_sum(self, n1, n2):
        total_sum = 0
        start = Calculator.sum(self, n1, 1)

        for i in range(start, n2):
            total_sum = Calculator.sum(self, i, total_sum)

        return total_sum

    def get_fibonacci(self, pos):
        if pos <= 0:
            raise Exception("Position provided is not positive integer")

        if pos == 1 or pos == 2:
            return 1

        previous_num = 1
        next_num = 1

        end = Calculator.sum(self, pos, 1)

        for i in range(3, end):
            current = Calculator.sum(self, previous_num, next_num)
            previous_num = next_num
            next_num = current

        return current

    def print_odd_strings(self, strings):
        list = []

        if not strings:
            raise Exception("There were no strings in the list")

        for i in range(0, len(strings), 2):
            print(strings[i])
            list.append(strings[i])

        return list
