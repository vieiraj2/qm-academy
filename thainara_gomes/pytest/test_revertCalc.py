from hamcrest import assert_that, equal_to
import pytest
from thainara_gomes.reverse_calculator import ReverseCalculator


# Inverte os valores de soma para subtração
@pytest.mark.parametrize('num1, num2, result', [
    (-1, 2, -2), (0, 0, 0), (1, 1, 0), (1, 0, 1), (1, 1, 0),
    (2, 1, 1), (2, 2, 0), (2, 5, 3), (3, 1, 2)])
def test_soma(num1, num2, result):
    calc = ReverseCalculator(num1, num2)
    assert_that(calc.sum(num1, num2), equal_to(result))


# Inverte os valores de soma para subtração
@pytest.mark.parametrize('num1, num2, result', [
    (-1, 2, -2), (0, 0, 0), (1, 1, 0), (1, 0, 1), (1, 1, 0),
    (2, 1, 1), (2, 2, 0), (2, 5, 3), (3, 1, 2)])
def test_sub(num1, num2, result):
    calc = ReverseCalculator(num1, num2)
    assert_that(calc.sub(num1, num2), equal_to(result))


# Inverte os valores de divisão para multiplicação
@pytest.mark.parametrize('num1, num2, result', [
    (-1, 2, -2), (0, 0, 0), (1, 1, 0), (1, 0, 1), (1, 1, 0),
    (2, 1, 1), (2, 2, 0), (2, 5, 3), (3, 1, 2)])
def test_div(num1, num2, result):
    calc = ReverseCalculator(num1, num2)
    assert_that(calc.div(num1, num2), equal_to(result))


# Inverte os valores de multiplicação para divisão
@pytest.mark.parametrize('num1, num2, result', [
    (-1, 2, -2), (0, 0, 0), (1, 1, 0), (1, 0, 1), (1, 1, 0),
    (2, 1, 1), (2, 2, 0), (2, 5, 3), (3, 1, 2)])
def test_multi(num1, num2, result):
    calc = ReverseCalculator(num1, num2)
    assert_that(calc.mult(num1, num2), equal_to(result))
