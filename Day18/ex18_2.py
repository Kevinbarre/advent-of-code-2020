import math
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))


def compute_parenthesis(expression):
    # print("Computing: {}".format(expression))
    last_opening = 0
    for i, c in enumerate(expression):
        if c == '(':
            last_opening = i
        elif c == ')':
            result = compute_no_parenthesis(expression[last_opening + 1:i])
            return expression[:last_opening] + str(result) + expression[i + 1:]
    # On a parcouru sans trouver de parenthèse
    return compute_no_parenthesis(expression)


def compute_no_parenthesis(expression):
    # print("Expression in compute no parenthesis:", expression)
    additions = expression.split(' * ')
    sums = [sum(int(value) for value in addition.split(' + ')) for addition in additions]
    product = math.prod(sums)
    # print("{} = {}".format(expression, product))
    return product


def compute_expression(expression):
    while True:
        expression = compute_parenthesis(expression)
        try:
            return int(expression)
        except ValueError:
            # Pas encore un resultat, on continue
            continue


total = 0
for line in lines:
    total += compute_expression(line)

print(total)
