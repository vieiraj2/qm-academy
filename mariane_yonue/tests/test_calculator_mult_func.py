import pytest
from hamcrest import assert_that, calling, equal_to, raises
from mariane_yonue.calculator_mult_func import CalculatorMultFunc


@pytest.mark.parametrize('n1, n2, expect', [
    (0, 0, 0),
    (0, 1, 0),
    (5, 6, 0),
    (1, 10, 44),
    (-2, 4, 5),
    (-10, -1, -44),
    (-6, -5, 0)])
def test_interval_sum(n1, n2, expect):
    assert_that(CalculatorMultFunc().interval_sum(n1, n2), equal_to(expect))


@pytest.mark.parametrize('pos, expect', [
    (1, 1),
    (2, 1),
    (6, 8),
    (65, 17167680177565)
])
def test_fibonacci(pos, expect):
    assert_that(CalculatorMultFunc().get_fibonacci(pos), equal_to(expect))


@pytest.mark.parametrize('pos', [0, -1])
def test_fibonacci_exception(pos):
    exception_message = "Position provided is not positive integer"
    get_fibonacci_method = CalculatorMultFunc().get_fibonacci

    assert_that(calling(get_fibonacci_method).with_args(pos),
                raises(Exception, exception_message))


@pytest.mark.parametrize('strings, expected_print', [
    (['a', 'b', 'c', 'd', 'e'], ['a', 'c', 'e']),
    (['c'], ['c']),
    (['b', 'c', 'e'], ['b', 'e']),
    (['ab', 'cd', 'ef', 'gh', 'ij'], ['ab', 'ef', 'ij'])])
def test_odd_positions(strings, expected_print):
    assert_that(CalculatorMultFunc().print_odd_strings(strings), equal_to(expected_print))


@pytest.mark.parametrize('strings', [[], None])
def test_odd_positions_exception(strings):
    exception_message = "There were no strings in the list"
    get_odd_method = CalculatorMultFunc().print_odd_strings

    assert_that(calling(get_odd_method).with_args(strings),
                raises(Exception, exception_message))
