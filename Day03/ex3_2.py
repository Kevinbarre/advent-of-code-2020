import sys

rows = []
for line in sys.stdin:
    cells = line.rstrip('\n')
    rows.append(cells)

# Largeur de la piste, pour savoir quand on arrive au bord et qu'on doit repartir à gauche
width = len(rows[0])


def count_trees(down, right):
    total = 0
    # Premier tour de boucle on regarde directement la position (down, right)
    j = right

    for i in range(down, len(rows), down):
        if rows[i][j] == '#':
            total += 1
        j = (j + right) % width

    return total


# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

result = 1
for slope in slopes:
    result *= count_trees(*slope)

print(result)
