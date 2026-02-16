# Team Name: Code trinity 

def calculate(expression: str) -> float:
    """
    Evaluate mathematical expression without using eval().

    Args:
        expression: Mathematical expression as string

    Returns:
        Result rounded to 2 decimal places
    """
    if not isinstance(expression, str):
        raise ValueError("expression must be a string.")
    expression = expression.replace(" ", "")

    if not expression:
        raise ValueError("expression cannot be empty.")

    numbers = []
    operators = []

    i = 0
    n = len(expression)

    while i < n:
        if expression[i].isdigit() or (
            expression[i] == '-' and 
            (i == 0 or expression[i - 1] in "+-*/")
        ):
            sign = 1
            if expression[i] == '-':
                sign = -1
                i += 1

            num = 0
            while i < n and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1

            numbers.append(sign * num)
        else:
            operators.append(expression[i])
            i += 1
    new_numbers = [numbers[0]]
    new_operators = []

    for idx, op in enumerate(operators):
        if op == '*':
            new_numbers[-1] = new_numbers[-1] * numbers[idx + 1]
        elif op == '/':
            new_numbers[-1] = new_numbers[-1] / numbers[idx + 1]
        else:
            new_numbers.append(numbers[idx + 1])
            new_operators.append(op)
    result = new_numbers[0]
    for idx, op in enumerate(new_operators):
        if op == '+':
            result += new_numbers[idx + 1]
        elif op == '-':
            result -= new_numbers[idx + 1]

    return round(float(result), 2)

