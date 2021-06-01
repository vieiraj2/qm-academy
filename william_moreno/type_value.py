# Challenge 2 - Type and value

import ast

value1 = None
value2 = None

# This exception treats cases where input is string. It is not accepted by 'ast.literal_eval' built in function
try:
    value1 = ast.literal_eval(input("Insira a primeira variável: "))
    value2 = ast.literal_eval(input("Insira a segunda variável: "))

except ValueError:
    value3 = None
    if type(value1) == type(value3):
        value1 = str(value1)
        value2 = ast.literal_eval(input("Insira a segunda variável: "))
    else:
        value2 = str(value2)


# This method shows the variable type
def typeAndValueUsingEval(value_a, value_b):
    print(type(value_a))
    print(type(value_b))


typeAndValueUsingEval(value1, value2)
