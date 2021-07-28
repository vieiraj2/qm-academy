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


# this method tests the method 'add' from multi_func_calculator -> CalculatorMultiFunc -> calculator -> Calculator
@pytest.mark.parametrize('a, b, expect', [
    (10, 10, 20),
    (-10, -15, -25),
    (10.5, 10.6, 21.1),
    (-10, 9, -1),
    (50, -10, 40), ])
def test_add(a, b, expect):
    op_object = CalculatorMultiFunc(a, b)
    assert_that(op_object.addition(), equal_to(expect))


# this method tests the method 'sub' from multi_func_calculator -> CalculatorMultiFunc -> calculator -> Calculator
@pytest.mark.parametrize('a, b, expect', [
    (10, 10, 0),
    (-10, -15, 5),
    (30, 9, 21),
    (50, -10, 60), ])
def test_sub(a, b, expect):
    op_object = CalculatorMultiFunc(a, b)
    assert_that(op_object.sub(), equal_to(expect))


# this method tests the method 'multiply' from multi_func_calculator -> CalculatorMultiFunc -> calculator -> Calculator
@pytest.mark.parametrize('a, b, expect', [
    (10, 10, 100),
    (-10, -15, 150),
    (30, 9, 270),
    (50, -10, -500), ])
def test_multiply(a, b, expect):
    op_object = CalculatorMultiFunc(a, b)
    assert_that(op_object.multiply(), equal_to(expect))


# this method tests the method 'divide' from multi_func_calculator -> CalculatorMultiFunc -> calculator -> Calculator
@pytest.mark.parametrize('a, b, expect', [
    (10, 10, 1),
    (-15, -10, 1.5),
    (30, 10, 3),
    (50, -10, -5), ])
def test_sub(a, b, expect):
    op_object = CalculatorMultiFunc(a, b)
    assert_that(op_object.divide(), equal_to(expect))
