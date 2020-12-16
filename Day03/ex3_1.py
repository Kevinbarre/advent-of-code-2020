import sys

rows = []
for line in sys.stdin:
    cells = line.rstrip('\n')
    rows.append(cells)

# Largeur de la piste, pour savoir quand on arrive au bord et qu'on doit repartir à gauche
width = len(rows[0])
total = 0
# Premier tour de boucle on regarde directement la position (1, 3)
j = 3

for i in range(1, len(rows)):
    if rows[i][j] == '#':
        total += 1
    j = (j + 3) % width

print(total)
