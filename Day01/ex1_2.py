import math
import sys
from itertools import combinations

# Somme à obtenir
SUM = 2020
# Nombre d'éléments pour obtenir la somme
NB_ELEM = 3

lines = []
for line in sys.stdin:
    lines.append(int(line.rstrip('\n')))

# On récupère la combinaison qui correspond à la somme
result = next(filter(lambda val: sum(val) == SUM, combinations(lines, NB_ELEM)))

# On affiche le produit
print(math.prod(result))
