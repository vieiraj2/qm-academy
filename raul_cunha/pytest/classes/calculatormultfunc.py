# !/usr/bin/env python3

from raul_cunha.pytest.classes.calculator import Calculator


class CalculatorMultFunc(Calculator):
    def __init__(self, oper1=None, oper2=None):
        # Just initializing the attributes
        self.oper1 = oper1
        self.oper2 = oper2
        super().__init__(oper1, oper2)

    def soma_interval(self):
        # This IF is just to let oper2 always bigger than oper1
        if self.oper2 < self.oper1:
            aux = self.oper1
            self.oper1 = self.oper2
            self.oper2 = aux
        lista = []
        if (self.oper2 - self.oper1 - 1) > 0:
            elemento = self.oper1 + 1
            while elemento < self.oper2:
                lista.append(elemento)
                elemento = elemento + 1
        soma_interval = 0
        for j in range(len(lista)):
            soma_interval = soma_interval + lista[j]
        return soma_interval

    def fibo(self):
        if self.oper1 <= 0:
            return None
        elif self.oper1 == 1:
            return 0
        elif self.oper1 == 2:
            return 1
        else:
            ant1 = 1
            ant2 = 0
            atual = ant1
            contador = 3
            while contador <= self.oper1:
                atual = ant1 + ant2
                ant2 = ant1
                ant1 = atual
                contador = contador + 1
            return atual

    def impares(self):
        if not self.oper1:
            return None
        lista_saida = []
        for j in range(len(self.oper1)):
            if j % 2 == 0:
                lista_saida.append(self.oper1[j])
        return lista_saida
