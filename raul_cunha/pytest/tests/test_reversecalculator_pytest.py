import pytest
from hamcrest import assert_that, equal_to

from raul_cunha.pytest.classes.reversecalculator import ReverseCalculator


# SOMA - CHECA RESULTADOS DO INVERSO OU SEJA DA SUBTRACAO:
@pytest.mark.parametrize('operador1, operador2, resultado', [
    (-1, 0, -1),
    (0, 0, 0),
    (0, -1, 1),
    (1, 0, 1),
    (0, 1, -1),
    (1, 1, 0),
    (1, 3, -2),
    (5, 3, 2)])
def test_soma(operador1, operador2, resultado):
    objcalc = ReverseCalculator(operador1, operador2)
    assert_that(objcalc.soma(), equal_to(resultado))


# SUBTRAI - CHECA RESULTADOS DO INVERSO OU SEJA DA SOMA:
@pytest.mark.parametrize('operador1, operador2, resultado', [
    (-1, 0, -1),
    (0, 0, 0),
    (0, -1, -1),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 2),
    (1, 3, 4),
    (5, 3, 8)])
def test_subtrai(operador1, operador2, resultado):
    objcalc = ReverseCalculator(operador1, operador2)
    assert_that(objcalc.subtrai(), equal_to(resultado))


# DIVIDE - CHECA RESULTADOS DO INVERSO OU SEJA DA MULTIPLICACAO:
@pytest.mark.parametrize('operador1, operador2, resultado', [
    (-1, 0, 0),
    (0, 0, 0),
    (0, -1, 0),
    (1, 0, 0),
    (0, 1, 0),
    (1, 1, 1),
    (1, 3, 3),
    (5, 3, 15)])
def test_divide(operador1, operador2, resultado):
    objcalc = ReverseCalculator(operador1, operador2)
    assert_that(objcalc.divide(), equal_to(resultado))


# MULTIPLICA - CHECA RESULTADOS DO INVERSO OU SEJA DA DIVISAO:
@pytest.mark.parametrize('operador1, operador2, resultado', [
    (1, 1, 1),
    (0, 1, 0),
    (1, 1, 1),
    (1, 2, 0.5),
    (3, 1, 3),
    (6, 3, 2)])
def test_multiplica(operador1, operador2, resultado):
    objcalc = ReverseCalculator(operador1, operador2)
    assert_that(objcalc.multiplica(), equal_to(resultado))
