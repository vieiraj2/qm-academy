class Calculator:
    # Função para soma
    def sum(self, num1, num2):
        soma = num1 + num2
        return soma

    # Função para subtração
    def sub(self, num1, num2):
        subt = num1 - num2
        return subt

    # Função para multiplicação
    def mult(self, num1, num2):
        mult = num1 * num2
        return mult

    # Função para divisão e tratamento de erro
    def div(self, num1, num2):
        try:
            div = num1 / num2
            return div
        except:
            print('Erro! Sistema não realiza divisão por zero')
