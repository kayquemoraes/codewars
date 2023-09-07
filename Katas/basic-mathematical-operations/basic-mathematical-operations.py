def basic_op(operator, value1, value2):
    operators = {
        '+':  value1 + value2,
        '-':  value1 - value2,
        '*':  value1 * value2,
        '/':  value1 / value2
    }
    return operators[operator]
    