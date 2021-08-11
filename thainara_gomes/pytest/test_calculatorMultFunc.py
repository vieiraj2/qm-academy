from hamcrest import assert_that, equal_to

import pytest
from thainara_gomes.calculatormultfunc import CalculatorMultFunc


@pytest.mark.parametrize('num1, num2, soma', [
    (-2, -2, 0), (-2, -1, 0), (-5, 5, 0),
    (2, 2, 0), (2, 3, 0), (2, 1, 0), (2, 5, 7),
    (5, 0, 10), (5, -5, 0)
])
def test_calculatorMultFunc(num1, num2, soma):
    result = CalculatorMultFunc(num1, num2)
    assert_that(result.sum(num1, num2), equal_to(soma))


# Mostra o elemento da sequencia de fibonacci
@pytest.mark.parametrize('posicao, elemento', {
    (1, 0), (2, 1), (3, 1), (4, 2),
    (5, 3), (6, 5), (7, 8), (8, 13)
})
def test_fibonacci(posicao, elemento):
    result = CalculatorMultFunc()
    assert_that(result.fibonacci(), equal_to(elemento))


# Realiza os testes de soma
@pytest.mark.parametrize('num1, num2, result', [
    (-1, 0, -1), (0, 0, 0), (0, -1, -1), (1, 0, 1),
    (0, 1, 1), (1, 1, 2), (1, 3, 4), (5, 3, 8)])
def test_soma(num1, num2, result):
    calc = CalculatorMultFunc(num1, num2)
    assert_that(calc.soma(), equal_to(result))


# Realiza os testes de subtração
@pytest.mark.parametrize('num1, num2, result', [
    (-1, 0, -1), (0, 0, 0), (0, -1, 1), (1, 0, 1),
    (0, 1, -1), (1, 1, 0), (1, 3, -2), (5, 3, 2)])
def test_sub(num1, num2, result):
    calc = CalculatorMultFunc(num1, num2)
    assert_that(calc.sub(num1, num2), equal_to(result))


# Realiza o teste de multiplicação
@pytest.mark.parametrize('num1, num2, result', [
    (-1, 0, 0), (0, 0, 0), (0, -1, 0), (1, 0, 0),
    (0, 1, 0), (1, 1, 1), (1, 3, 3), (5, 3, 15)])
def test_multiplicacao(num1, num2, result):
    calc = CalculatorMultFunc(num1, num2)
    assert_that(calc.mult(num1, num2), equal_to(result))


# Realiza o teste de divisão
@pytest.mark.parametrize('num1, num2, result', [
    (1, 1, 1), (0, 1, 0), (1, 1, 1),
    (1, 2, 0.5), (3, 1, 3), (6, 3, 2)])
def test_div(num1, num2, result):
    calc = CalculatorMultFunc(num1, num2)
    assert_that(calc.div(num1, num2, ), equal_to(result))


# Posições dos elementos
@pytest.mark.parametrize('entrada,saida', [
    (['1°'], ['1°']),
    (['1°', '2°'], ['1°']),
    (['1°', '2°', '3°'], ['1°', '3°']),
    (['1°', '2°', '3°', '4°'], ['1°', '3°']),
    (['1°', '2°', '3°', '4°', '5°'], ['1°', '3°', '5°']),
    (['1°', '2°', '3°', '4°', '5°', '6°'], ['1°', '3°', '5°']),
    (['1°', '2°', '3°', '4°', '5°', '6°', '7°'],
     ['1°', '3°', '5°', '7°']),
])
def test_impar(entrada, saida):
    calc = CalculatorMultFunc(entrada)
    assert_that(calc.impar(), equal_to(saida))
