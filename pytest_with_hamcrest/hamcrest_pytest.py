"""
Some of these methods contain errors, find this by Pytest and using the PyHamcrest on Assert!
After get the results from
"""
import random
import string
from random import randint


def string_with_more_than_x_characters(characters_quantity):
    """string_with_more_than_x_characters(characters_quantity) -> String """
    _len = randint(0, 10) + characters_quantity
    letters = string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(_len))
    print('Random string of length', _len, 'is:', result)
    return result


def string_with_more_less_x_characters(characters_quantity):
    """string_with_more_less_x_characters(characters_quantity) -> String """
    _len = characters_quantity - randint(0, 10)
    letters = string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(_len))
    print('Random string of length', _len, 'is:', result)
    return result


def int_bigger_than_x(x_value):
    """int_bigger_than_x(x_value) -> int """
    y_value = x_value * -1 if x_value < 0 else x_value
    value = x_value + randint(y_value, y_value + 1)
    print(value)
    return value


def int_less_than_x(x_value):
    """int_less_than_x(x_value) -> int """
    y_value = x_value * -1 if x_value < 0 else x_value
    value = x_value - randint(1, y_value)
    print(value)
    return value


def return_a_phrase_with_24_characters_plus_our_name(name):
    """return_a_phrase_with_24_characters_plus_our_name(name) -> string """
    return 'Maybe this is your name: ' + name


def number_list_with_the_same_value():
    """number_list_with_the_same_value() -> list """
    return [1, 1, 1, 1, 1, 1, 1]


def string_list_with_the_same_value():
    """string_list_with_the_same_value() -> list """
    return ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar']


def characters_list_with_the_all_values():
    """characters_list_with_the_all_values() -> list """
    return list(string.printable)


def characters_list_with_the_letters_values():
    """characters_list_with_the_letters_values() -> list """
    return list(string.ascii_letters)


def characters_list_with_the_numbers_values():
    """characters_list_with_the_numbers_values() -> list """
    return list(string.digits)
