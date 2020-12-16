import sys

lines = []
for line in sys.stdin:
    lines.append(int(line.rstrip('\n')))

lines = sorted(lines)

first = lines.pop(0)
last = lines.pop(-1)

while True:
    sum = first + last

    if sum == 2020:
        # Trouvé ! On print la multiplication des deux
        print(first * last)
        break
    elif sum > 2020:
        # On a dépassé, c'est donc qu'il faut réduire le dernier élément
        last = lines.pop(-1)
    else:
        # On n'est pas assez haut, c'est donc qu'il faut augmenter le premier élément
        first = lines.pop(0)
