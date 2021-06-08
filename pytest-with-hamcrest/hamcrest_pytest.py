import random
import string
from random import randint


# Some of these methods contain errors, find this by Pytest and using the PyHamcrest on Assert!
# After get the results from

def string_with_more_than_x_characters(characters_quantity):
    _len = randint(0, 10) + characters_quantity
    letters = string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(_len))
    print("Random string of length", _len, "is:", result)
    return result


def string_with_more_less_x_characters(characters_quantity):
    _len = characters_quantity - randint(0, 10)
    letters = string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(_len))
    print("Random string of length", _len, "is:", result)
    return result


def int_bigger_than_x(x):
    y = x * -1 if x < 0 else x
    value = x + randint(y, y+1)
    print(value)
    return value


def int_less_than_x(x):
    y = x * -1 if x < 0 else x
    value = x - randint(1, y)
    print(value)
    return value


def return_a_frase_with_24_characters_plus_our_name(name):
    return "Maybe this is your name: " + name


def number_list_with_the_same_value():
    return [1, 1, 1, 1, 1, 1, 1]


def string_list_with_the_same_value():
    return ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar']


def characters_list_with_the_all_values():
    return list(string.printable)


def characters_list_with_the_letters_values():
    return list(string.ascii_letters)


def characters_list_with_the_numbers_values():
    return list(string.digits)


print(int_bigger_than_x(5))
