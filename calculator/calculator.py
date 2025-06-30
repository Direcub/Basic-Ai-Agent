import re

def calculate(expression):
    def precedence(operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        return 0

    def apply_op(num1, num2, operator):
        if operator == '+': return num1 + num2
        if operator == '-': return num1 - num2
        if operator == '*': return num1 * num2
        if operator == '/': return num1 / num2
        return 0

    tokens = re.findall(r'(\d+|\+|\-|\*|\/)', expression)
    values = []
    ops = []
    i = 0
    while i < len(tokens):
        if tokens[i].isdigit():
            values.append(int(tokens[i]))
        elif tokens[i] in ['+', '-', '*', '/']:
            while ops and precedence(ops[-1]) >= precedence(tokens[i]):
                num2 = values.pop()
                num1 = values.pop()
                op = ops.pop()
                values.append(apply_op(num1, num2, op))
            ops.append(tokens[i])
        i += 1

    while ops:
        num2 = values.pop()
        num1 = values.pop()
        op = ops.pop()
        values.append(apply_op(num1, num2, op))

    return values[-1]

if __name__ == "__main__":
    expression = "3+7*2"
    result = calculate(expression)
    print(f"{expression} = {result}")
    expression2 = "10 - 2 / 2"
    result2 = calculate(expression2)
    print(f"{expression2} = {result2}")
