from sergio_granzotti.calculatorMultFunc import calculatorMultFunc
import pytest  # importa pytest
from hamcrest import assert_that, equal_to


@pytest.mark.parametrize('n1, n2, expect', [
    (2, 2, 4),
    (5, 10, 15),
    (-8, 3, -5),
    (-6, -3, -9),
    (-4, 12, 8), ])
# Esse metodo testa o metodo sum da classe calculator
# O resultado esperado eh a soma de n1+n2
def test_calculator_sum(n1, n2, expect):
    result = calculatorMultFunc(n1, n2)
    assert_that(result.sum(), equal_to(expect))


@pytest.mark.parametrize('n1, n2, expect', [
    (2, 2, 0),
    (5, 10, -5),
    (-8, 3, -11),
    (20, 3, 17),
    (6, 3, 3), ])
# Esse metodo testa o metodo sum da classe calculator
# O resultado esperado eh a subtração de n1-n2
def test_calculator_sub(n1, n2, expect):
    result = calculatorMultFunc(n1, n2)
    assert_that(result.sub(), equal_to(expect))


@pytest.mark.parametrize('n1, n2, expect', [
    (2, 3, 6),
    (5, 10, 50),
    (9, 3, 27),
    (11, 4, 44),
    (21, 3, 63), ])
# Esse metodo testa o metodo sum da classe calculator
# O resultado esperado eh a multiplicação de n1*n2
def test_calculator_mult(n1, n2, expect):
    result = calculatorMultFunc(n1, n2)
    assert_that(result.mult(), equal_to(expect))


@pytest.mark.parametrize('n1, n2, expect', [
    (10, 2, 5),
    (20, 4, 5),
    (36, 3, 12),
    (9, 1, 9),
    (26, 13, 2), ])
# Esse metodo testa o metodo sum da classe calculator
# O resultado esperado eh a divisao de n1/n2
def test_calculator_div(n1, n2, expect):
    result = calculatorMultFunc(n1, n2)
    assert_that(result.div(), equal_to(expect))
