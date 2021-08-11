from hamcrest import assert_that, equal_to

import pytest
from thainara_gomes.calculatormultfunc import CalculatorMultFunc


@pytest.mark.parametrize('num1, num2, soma', [
    (2, -2, 0), (-2, -1, -3), (-5, 5, 0),
    (2, -2, 0), (-2, 3, 1), (2, -1, 1), (2, 5, 7),
    (5, -3, 2), (5, -5, 0)
])
def test_calculatorMultFunc(num1, num2, soma):
    result = CalculatorMultFunc(num1, num2)
    assert_that(result.sum(), equal_to(soma))
