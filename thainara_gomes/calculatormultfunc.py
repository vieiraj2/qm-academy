from thainara_gomes.calculator import Calculator


class CalculatorMultFunc(Calculator):
    def __init__(self, num1=None, num2=None):
        self.num1 = num1
        self.num2 = num2
        super().__init__(num1, num2)

    def soma(self):
        if self.num2 < self.num1:
            aux = self.num1
            self.num1 = self.num2
            self.num2 = aux
        lista = []
        if (self.num2 - self.num1 - 1) > 0:
            element = self.num1 + 1
            while element < self.num2:
                lista.append(element)
                element = element + 1
        soma = 0
        for n in range(len(lista)):
            soma = soma + lista[n]
        return soma

    def fibonacci(self):
        if self.num1 <= 0:
            return None
        elif self.num1 == 1:
            return 0
        elif self.num1 == 2:
            return 1
        else:
            fib1 = 1
            fib2 = 0
            result = fib1
            cont = 3
            while cont <= self.num1:
                result = fib1 + fib2
                fib2 = fib1
                fib1 = result
                cont = cont + 1
            return result

    def impar(self):
        if not self.num1:
            return None
        saida = []
        for n in range(len(self.num1)):
            if n % 2 == 0:
                saida.append(self.num1[n])
        return saida
