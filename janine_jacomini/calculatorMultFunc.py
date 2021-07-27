from calculator import Calculator


class calculatorMultFunc(Calculator):

    # Soma intervalo
    def item_1(self, n1, n2):
        sunInterval = 0
        for x in range(n1 + 1, n2):
            sunInterval = sunInterval + x
        return sunInterval

    # Fibonacci
    def item_2(self, n1):
        proximo = 0
        anterior = 0
        index = 0
        while n1 > index:
            index = index + 1
            proximo = proximo + anterior
            anterior = proximo - anterior
            if proximo == 0:
                proximo = proximo + 1
        return proximo

    # Print odd
    def item_3(self, n1):
        oddList = []
        index = 0
        while index < len(n1):
            if (index % 2) == 0:
                print(n1[index], end=' ')
                oddList.append(n1[index])
            index = index + 1
            print(oddList)
        return oddList
