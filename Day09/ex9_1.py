import sys
from itertools import combinations

numbers = []
for line in sys.stdin:
    numbers.append(int(line.rstrip('\n')))

SIZE = 25


def is_valid(number, preamble):
    try:
        next(filter(lambda val: sum(val) == number, combinations(preamble, 2)))
        return True
    except StopIteration:
        return False


for i in range(SIZE, len(numbers)):
    number = numbers[i]
    if not is_valid(number, numbers[i - SIZE:i]):
        print(number)
        break
