class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Função para soma
    def sum(self):
        soma = self.num1 + self.num2
        return soma

    # Função para subtração
    def sub(self):
        subt = self.num1 - self.num2
        return subt

    # Função para multiplicação
    def mult(self):
        mult = self.num1 * self.num2
        return mult

    # Função para divisão e tratamento de erro
    def div(self):
        try:
            div = self.num1 / self.num2
            return div

        except ZeroDivisionError:
            print('Erro! Sistema não realiza divisão por zero')
