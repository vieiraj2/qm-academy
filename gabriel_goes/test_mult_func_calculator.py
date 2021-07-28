import pytest
from hamcrest import assert_that, equal_to
from multi_func_calculator import CalculatorMultiFunc


# This method tests the 'interval_sum' method from multi_func_calculator -> CalculatorMultiFunc
@pytest.mark.parametrize('a, b, expect', [
    (10, 15, 50),
    (-10, 5, -35),
    (-1, 2, 1),
    (0, 0, 0),
    (-10, 10, 0), ])
def test_sum_interval(a, b, expect):
    interval_result = CalculatorMultiFunc(a, b)
    assert_that(interval_result.interval_sum(a, b), equal_to(expect))


# This method tests the 'fibonacci' method from multi_func_calculator -> CalculatorMultiFunc
@pytest.mark.parametrize('a, expect', [
    (1, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8), ])
def test_fibonacci(a, expect):
    fibonacci_result = CalculatorMultiFunc(a, 0)
    assert_that(fibonacci_result.fibonacci(a), equal_to(expect))


# This method tests the 'print_odd_list' method from multi_func_calculator -> CalculatorMultiFunc
@pytest.mark.parametrize('a, expect', [
    (['a', 'b'], ['a']),
    (['a', 'b', 'c', 'd'], ['a', 'c']),
    (['a', 'b', 'c', 'd', 'e'], ['a', 'c', 'e']),
    (['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['a', 'c', 'e', 'g']),
    (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], ['a', 'c', 'e', 'g', 'i']), ])
def test_odd(a, expect):
    odd_result = CalculatorMultiFunc(a, 0)
    assert odd_result.print_odd_list(a) == expect
