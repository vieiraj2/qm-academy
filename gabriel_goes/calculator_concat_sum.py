from calculator import Calculator


class CalculatorConcatSum (Calculator):
    def addition(self):
        num_a = self.a
        num_b = self.b

        cct = (str(num_a) + str(num_b))
        print('Concatenating {} and {} results on {}'.format(self.a, self.b, cct))
        return cct
