import math
import sys

numbers = []
for line in sys.stdin:
    numbers.append(int(line.rstrip('\n')))


def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


numbers = sorted(numbers)

current = 0
nb_ones = []
current_nb_one = 0

for number in numbers:
    difference = number - current
    if difference == 1:
        current_nb_one += 1
    else:
        # Pas de difference de 1, on reprend le compte
        if current_nb_one > 0:
            nb_ones.append(tribonacci(current_nb_one + 1))
        current_nb_one = 0
    current = number

# On ajoute la dernière différence
if current_nb_one > 0:
    nb_ones.append(tribonacci(current_nb_one + 1))

print(math.prod(nb_ones))
