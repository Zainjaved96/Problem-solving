def multiply(a, b):
    return a * b


def calculate(*values, operator):
    return operator(*values)


cal = calculate(5, 6, operator=multiply)
print(cal)
