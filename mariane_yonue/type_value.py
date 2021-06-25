def print_types(first_input, second_input):
    try:
        first_type = type(eval(first_input))

    except:
        first_type = type('String')

    try:
        second_type = type(eval(second_input))

    except:
        second_type = type('String')

    print("The first value type is {} and the second one is {}".format(first_type, second_type))

first_input = input("Input the first value:")
second_input = input("Input the second value:")

print_types(first_input, second_input)