from hamcrest import assert_that, equal_to
from ana_borges.ReverseCalculator import ReverseCalculator
import pytest


@pytest.mark.parametrize('n1,n2,expect', [
    (1, 2, -1),
    (1.5, -0.5, 2.0),
    (-4, 2, -6),
    (2, 1, 1),
    (-0.5, -6.0, 5.5)])
def test_reverse_sum(n1, n2, expect):
    assert_that(ReverseCalculator().sum(n1, n2), equal_to(expect))


@pytest.mark.parametrize('n1,n2,expect', [
    (1, 2, 3),
    (1.5, -0.5, 1.0),
    (-4, 2, -2),
    (2, -1, 1),
    (-0.5, -6.0, -6.5)])
def test_reverse_sub(n1, n2, expect):
    assert_that(ReverseCalculator().sub(n1, n2), equal_to(expect))


@pytest.mark.parametrize('n1,n2,expect', [
    (1, 2, 0.5),
    (1.5, -0.5, -3),
    (-4, 2, -2),
    (2, -1, -2),
    (-6.0, 0.5, -12)])
def test_reverse_mult(n1, n2, expect):
    assert_that(ReverseCalculator().multi(n1, n2), equal_to(expect))


@pytest.mark.parametrize('n1,n2,expect', [
    (1, 2, 2),
    (1.5, -0.5, -0.75),
    (-4, 2, -8),
    (2, -1, -2),
    (-6.0, 0.5, -3),
    (0, 5, 0)])
def test_reverse_div(n1, n2, expect):
    assert_that(ReverseCalculator().div(n1, n2), equal_to(expect))
