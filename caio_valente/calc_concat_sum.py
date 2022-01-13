from calculator import Calculator

class CalcConcatSum (Calculator):
    def sum(self):
        int_n1 = int(self.value1)
        int_n2 = int(self.value2)
        concat = float(str(int_n1) + str(int_n2))
        print (f"the concatenation from this 2 numbers is: {self.value1} concat {self.value2} = {concat}")
        return concat