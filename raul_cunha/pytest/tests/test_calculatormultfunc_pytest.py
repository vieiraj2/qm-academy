import pytest
from hamcrest import assert_that, equal_to

from raul_cunha.pytest.classes.calculatormultfunc import CalculatorMultFunc


# DADOS DOIS INTEIROS, CALCULA A SOMA DOS NUMEROS CONTIDOS NO INTERVALO ENTRE OS MESMOS:
@pytest.mark.parametrize('operador1, operador2, soma_interval', [
    (-2, -2, 0),
    (-2, -1, 0),
    (-2, -3, 0),
    (-5, -3, -4),
    (-5, -2, -7),
    (-5, 0, -10),
    (-5, 5, 0),
    (0, -5, -10),
    (2, 2, 0),
    (2, 3, 0),
    (2, 1, 0),
    (2, 5, 7),
    (5, 0, 10),
    (5, -5, 0)
])
def test_soma_interval(operador1, operador2, soma_interval):
    objcalc = CalculatorMultFunc(operador1, operador2)
    assert_that(objcalc.soma_interval(), equal_to(soma_interval))


# IDENTIFICA O ELEMENTO DE UMA DADA POSICAO NA SEQUENCIA DE FIBONACCI:
@pytest.mark.parametrize('posicao, elemento', {
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (7, 8),
    (8, 13),
    (9, 21),
    (10, 34),
    (11, 55),
    (12, 89),
    (13, 144)
})
def test_fibo(posicao, elemento):
    objcalc = CalculatorMultFunc(posicao)
    assert_that(objcalc.fibo(), equal_to(elemento))


# A PARTIR DE UMA LISTA DE STRINGS, IMPRIME AS STRINGS CUJA POSICAO SEJA IMPAR NA LISTA DE ENTRADA:
@pytest.mark.parametrize('lista_entrada, lista_saida', [
    (['primeiro'], ['primeiro']),
    (['primeiro', 'segundo'], ['primeiro']),
    (['primeiro', 'segundo', 'terceiro'], ['primeiro', 'terceiro']),
    (['primeiro', 'segundo', 'terceiro', 'quarto'], ['primeiro', 'terceiro']),
    (['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto'], ['primeiro', 'terceiro', 'quinto']),
    (['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto'], ['primeiro', 'terceiro', 'quinto']),
    (['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'setimo'], ['primeiro', 'terceiro', 'quinto', 'setimo']),
])
def test_lista_posicoes_impares(lista_entrada, lista_saida):
    objcalc = CalculatorMultFunc(lista_entrada)
    assert_that(objcalc.impares(), equal_to(lista_saida))


# DADOS DOIS INTEIROS, CALCULA A SOMA DOS MESMOS, A PARTIR DO METODO HERDADO DA CLASSE PAI
@pytest.mark.parametrize('operador1, operador2, resultado', [
    (-1, 0, -1),
    (0, 0, 0),
    (0, -1, -1),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 2),
    (1, 3, 4),
    (5, 3, 8)])
def test_soma_classe_pai(operador1, operador2, resultado):
    objcalc = CalculatorMultFunc(operador1, operador2)
    assert_that(objcalc.soma(), equal_to(resultado))


# DADOS DOIS INTEIROS, CALCULA A SUBTRACAO DOS MESMOS, A PARTIR DO METODO HERDADO DA CLASSE PAI
@pytest.mark.parametrize('operador1, operador2, resultado', [
    (-1, 0, -1),
    (0, 0, 0),
    (0, -1, 1),
    (1, 0, 1),
    (0, 1, -1),
    (1, 1, 0),
    (1, 3, -2),
    (5, 3, 2)])
def test_subtrai_classe_pai(operador1, operador2, resultado):
    objcalc = CalculatorMultFunc(operador1, operador2)
    assert_that(objcalc.subtrai(), equal_to(resultado))


# DADOS DOIS INTEIROS, CALCULA A MULTIPLICACAO DOS MESMOS, A PARTIR DO METODO HERDADO DA CLASSE PAI
@pytest.mark.parametrize('operador1, operador2, resultado', [
    (-1, 0, 0),
    (0, 0, 0),
    (0, -1, 0),
    (1, 0, 0),
    (0, 1, 0),
    (1, 1, 1),
    (1, 3, 3),
    (5, 3, 15)])
def test_multiplica_classe_pai(operador1, operador2, resultado):
    objcalc = CalculatorMultFunc(operador1, operador2)
    assert_that(objcalc.multiplica(), equal_to(resultado))


# DADOS DOIS INTEIROS, CALCULA A DIVISAO DOS MESMOS, A PARTIR DO METODO HERDADO DA CLASSE PAI
@pytest.mark.parametrize('operador1, operador2, resultado', [
    (1, 1, 1),
    (0, 1, 0),
    (1, 1, 1),
    (1, 2, 0.5),
    (3, 1, 3),
    (6, 3, 2)])
def test_divide_classe_pai(operador1, operador2, resultado):
    objcalc = CalculatorMultFunc(operador1, operador2)
    assert_that(objcalc.divide(), equal_to(resultado))
