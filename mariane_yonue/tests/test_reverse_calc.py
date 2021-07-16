import pytest
from hamcrest import assert_that, equal_to
from mariane_yonue.reverse_calculator import ReverseCalculator


@pytest.mark.parametrize('n1, n2, expect', [
    (2, 1, 1),
    (1, 2, -1),
    (-4, 2, -6),
    (1.5, -0.5, 2.0),
    (-0.5, -6.0, 5.5)])
def test_reverse_sum(n1, n2, expect):
    assert_that(ReverseCalculator().sum(n1, n2), equal_to(expect))


@pytest.mark.parametrize("n1,n2,expect", [
    (1, 2, 3),
    (2, -1, 1),
    (-4, 2, -2),
    (1.5, -0.5, 1.0),
    (-0.5, -6.0, -6.5)])
def test_reverse_sub(n1, n2, expect):
    assert_that(ReverseCalculator().sub(n1, n2), equal_to(expect))


@pytest.mark.parametrize('n1, n2, expect', [
    (1, 2, 0.5),
    (4, -4, -1),
    (-6, -3, 2),
    (5, 1, 5),
    (-1.5, 0.5, -3)])
def test_reverse_mult(n1, n2, expect):
    assert_that(ReverseCalculator().mult(n1, n2), equal_to(expect))


@pytest.mark.parametrize('n1, n2, expect', [
    (1, 2, 2),
    (4, -4, -16),
    (-6, -3, 18),
    (5, 0, 0),
    (-1.5, 0.5,-0.75),
    (2.5, 4.0, 10)])
def test_reverse_div(n1, n2, expect):
    assert_that(ReverseCalculator().div(n1, n2), equal_to(expect))
