from janine_jacomini.reverseCalculator import ReverseCalculator
import pytest  # importa pytest
from hamcrest import assert_that, equal_to


@pytest.mark.parametrize('n1, n2, expect', [
    (2, 1, 1),
    (5, -2, 7),
    (5, 3, 2),
    (-5, -3, -2),
    (-4, 8, -12), ])
# Esse metodo testa o metodo sum da classe reverseCalculator
# O resultado esperado eh a subtração de n1-n2
def test_reverse_sum(n1, n2, expect):
    a = ReverseCalculator(n1, n2)
    assert_that(a.sum(), equal_to(expect))


@pytest.mark.parametrize('n1, n2, expect', [
    (2, 2, 4),
    (-5, -4, -9),
    (6.1, 2.4, 8.5),
    (-2, 6, 4),
    (8, 9, 17), ])
# Esse metodo testa o metodo sum da classe reverseCalculator
# O resultado esperado eh a soma de n1+n2
def test_reverse_sub(n1, n2, expect):
    a = ReverseCalculator(n1, n2)
    assert_that(a.sub(), equal_to(expect))


@pytest.mark.parametrize('n1, n2, expect', [
    (10, 2, 5),
    (8, 2, 4),
    (22, 4, 5.5),
    (750, 6, 125),
    (98, 4, 24.5), ])
# Esse metodo testa o metodo sum da classe reverseCalculator
# O resultado esperado eh a divisao de n1/n2
def test_reverse_mult(n1, n2, expect):
    a = ReverseCalculator(n1, n2)
    assert_that(a.mult(), equal_to(expect))


@pytest.mark.parametrize('n1, n2, expect', [
    (2, 5, 10),
    (-12, -3, 36),
    (20, 5, 100),
    (231, 2, 462),
    (-2, 5, -10), ])
# Esse metodo testa o metodo sum da classe reverseCalculator
# O resultado esperado eh a multiplicacao de n1*n2
def test_reverse_div(n1, n2, expect):
    a = ReverseCalculator(n1, n2)
    assert_that(a.div(), equal_to(expect))
