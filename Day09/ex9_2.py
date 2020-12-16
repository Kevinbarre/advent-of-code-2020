import sys
from itertools import combinations

numbers = []
for line in sys.stdin:
    numbers.append(int(line.rstrip('\n')))

# INVALID_NUMBER = 127
INVALID_NUMBER = 1038347917

# On précalcule la somme des différents nombres consécutifs à partir du premier
precalc = [0]
for number in numbers:
    last = precalc[-1]
    precalc.append(last + number)

# On cherche la combinaison égale à notre nombre invalid
x, y = next(
    filter(lambda combination: abs(combination[0] - combination[1]) == INVALID_NUMBER, combinations(precalc, 2)))

# print(combination)

# On récupère les indexes de notre combinaison
first_index = precalc.index(x)
second_index = precalc.index(y)

weakness = numbers[first_index:second_index]

print(weakness)

print(min(weakness) + max(weakness))
