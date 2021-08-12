from sergio_granzotti.calculatorMultFunc import calculatorMultFunc
import pytest  # importa pytest
from hamcrest import assert_that, equal_to


@pytest.mark.parametrize('n1,n2,expect', [
    (1, 10, 44),
    (2, 8, 25),
    (-3, 5, 7),
    (0, 3, 3),
    (3, 11, 49), ])
# Esse metodo testa o metodo item_1 da calculatorMultFunc
# Soma o intervala entre os numeros contidos no intervalo
def test_sum_interval(n1, n2, expect):
    v2 = calculatorMultFunc(n1, n2)
    assert_that(v2.item_1(n1, n2), equal_to(expect))


@pytest.mark.parametrize('n1,expect', [
    (1, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8), ])
# Esse metodo testa o metodo item_2 da calculatorMultFunc
# Dada a posição, imprime o elemento correspondente a sequência de Fibonacci
def test_posicao_fibonacci(n1, expect):
    v3 = calculatorMultFunc(n1, 0)
    assert_that(v3.item_2(n1), equal_to(expect))


@pytest.mark.parametrize('n1,expect', [
    (['a', 'b'], ['a']),
    (['a', 'b', 'c', 'd'], ['a', 'c']),
    (['a', 'b', 'c', 'd', 'e'], ['a', 'c', 'e']),
    (['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['a', 'c', 'e', 'g']),
    (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], ['a', 'c', 'e', 'g', 'i']), ])
# Esse metodo testa o metodo item_3 da calculatorMultFunc
# Receba uma lista de strings e imprima todas as posições ímpares
def test_posicao_odd(capsys, n1, expect):
    v3 = calculatorMultFunc(n1, 0)
    # v3.item_3(n1)
    # captured = capsys.readouterr()
    assert v3.item_3(n1) == expect
