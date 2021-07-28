import pytest
from hamcrest import assert_that, equal_to
from reverse_calculator import ReverseCalculator


# this method tests the method 'addition' from reverse_calculator -> ReverseCalculator
@pytest.mark.parametrize('a, b, expect', [
    (10, 1, 9),
    (10, 3, 7),
    (10, -3, 13),
    (-10, -10, 0),
    (-10, 5, -15), ])
def test_reverse_addition(a, b, expect):
    a = ReverseCalculator(a, b)
    assert_that(a.addition(), equal_to(expect))


# this method tests the method 'sub' from reverse_calculator -> ReverseCalculator
@pytest.mark.parametrize('a, b, expect', [
    (10, 10, 20),
    (-10, -15, -25),
    (10.5, 10.6, 21.1),
    (-10, 9, -1),
    (50, -10, 40), ])
def test_reverse_sub(a, b, expect):
    a = ReverseCalculator(a, b)
    assert_that(a.sub(), equal_to(expect))


# this method tests the method 'multiply' from reverse_calculator -> ReverseCalculator
@pytest.mark.parametrize('a, b, expect', [
    (10, 10, 1),
    (-10, -5, 2),
    (10.5, 2.5, 4.2),
    (-10, 2, -5),
    (50, -10, -5), ])
def test_reverse_multiply(a, b, expect):
    a = ReverseCalculator(a, b)
    assert_that(a.multiply(), equal_to(expect))


# this method tests the method 'divide' from reverse_calculator -> ReverseCalculator
@pytest.mark.parametrize('a, b, expect', [
    (10, 10, 100),
    (-10, -5, 50),
    (10.5, 2.5, 26.25),
    (-10, 2, -20),
    (50, -10, -500), ])
def test_reverse_divide(a, b, expect):
    a = ReverseCalculator(a, b)
    assert_that(a.divide(), equal_to(expect))
