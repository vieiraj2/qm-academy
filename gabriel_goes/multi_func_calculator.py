from calculator import Calculator


class CalculatorMultiFunc(Calculator):

    # Sum interval
    def interval_sum(self, a, b):
        sum_interval = 0
        for x in range(a + 1, b):
            sum_interval = sum_interval + x
        return sum_interval

    # Fibonacci
    def fibonacci(self, a):
        next_number = 0
        previous = 0
        index = 0
        while a > index:
            index = index + 1
            next_number = next_number + previous
            previous = next_number - previous
            if next_number == 0:
                next_number = next_number + 1
        return next_number

    # Print odd
    def print_odd_list(self, a):
        list_odd = []
        index = 0
        while index < len(a):
            if (index % 2) == 0:
                print(a[index], end=' ')
                list_odd.append(a[index])
            index = index + 1
            print(list_odd)
        return list_odd
