from reverse_calculator import ReverseCalc
from calculator_mult_func import CalculatorMultFunc
import pytest
from hamcrest import assert_that, equal_to


@pytest.mark.parametrize('value1, value2, expected',
                         [(1, 1, 0), (10, 5, 5), (7, 3, 4),
                          (-10, 10, -20), (-50, 40, -90), (50, -40, 90)])
def test_sum_inverse_calc(value1, value2, expected):
    assert_that(ReverseCalc().soma(value1, value2), equal_to(expected))


@pytest.mark.parametrize('value1, value2, expected',
                         [(10, 10, 20), (10, -5, 5), (1100, 1150, 2250),
                          (15, 15, 30), (-10, -10, -20), (-50, 100, 50)])
def test_sub_inverse_calc(value1, value2, expected):
    assert_that(ReverseCalc().sub(value1, value2), equal_to(expected), 'It is only a simple test')


@pytest.mark.parametrize('value1, value2, expected',
                         [(10, 10, 1), (10, -5, -2), (1100, 1150, 0.9565217391304348),
                          (15, 15, 1), (-10, -10, 1), (-50, 100, -0.5)])
def test_mult_inverse_calc(value1, value2, expected):
    assert_that(ReverseCalc().mult(value1, value2), equal_to(expected), 'It is only a simple test')


@pytest.mark.parametrize('value1, value2, expected',
                         [(10, 10, 100), (10, -5, -50), (1100, 1150, 1265000),
                          (15, 15, 225), (-10, -10, 100), (-50, 100, -5000)])
def test_div_inverse_calc(value1, value2, expected):
    assert_that(ReverseCalc().div(value1, value2), equal_to(expected), 'It is only a simple test')


@pytest.mark.parametrize('value1, value2, expected',
                         [(1, 10, '23456789'), (5, 20, '678910111213141516171819'),
                          (100, 113, '101102103104105106107108109110111112'), (1, 3, '2'),
                          (9, 19, '101112131415161718')])
def test_concateneted_calc(value1, value2, expected):
    assert_that(CalculatorMultFunc().concateneted_sum(value1, value2), equal_to(expected))


@pytest.mark.parametrize('value1, expected',
                         [(1, 1), (2, 1), (3, 2),
                          (100, 354224848179261915075), (10, 55),
                          (17, 1597), (21, 10946)])
def test_fibo(value1, expected):
    assert_that(CalculatorMultFunc().fibonacci(value1), equal_to(expected))


@pytest.mark.string_list
@pytest.mark.parametrize('value1, expected',
                         [('ola sou rayan', ['l', ' ', 'o', ' ', 'a', 'a']),
                          ('abcde', ['b', 'd']), ('ab', ['b']),
                          ('abcdefghijklmnopqrstuvwxyz',
                           ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z'])])
def test_list_of_string(value1, expected):
    assert_that(CalculatorMultFunc().list_of_string(value1), equal_to(expected))
