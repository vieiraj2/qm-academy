def valType (value1, value2):
    try:
        firstType = type(eval(value1))
    except:
        firstType = type('String')

    try:
        secondType = type(eval(value2))
    except:
        secondType = type('String')
    print("The first value is a {} and the second is a {}".format(firstType, secondType))

val1 = input("Type something: ")
val2 = input("Type something: ")

valType(val1, val2)