def which_type():
    inputs = (1, 45.9, 'one', [2, 3], True, {'Test': 1}, (1, 2, 3), None)
    for i in inputs:
        print('The element "{}" type is {}'.format(i, type(i)))


which_type()
