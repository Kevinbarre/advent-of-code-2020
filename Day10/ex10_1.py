import sys

numbers = []
for line in sys.stdin:
    numbers.append(int(line.rstrip('\n')))

numbers = sorted(numbers)

current = 0

nb_one = 0
nb_three = 1 # The last difference is always 3

for number in numbers:
    difference = number - current
    if difference == 1:
        nb_one += 1
    elif difference == 3:
        nb_three += 1
    current = number

# print("Nb 1 : {}".format(nb_one))
# print("Nb 3 : {}".format(nb_three))
print(nb_one * nb_three)
