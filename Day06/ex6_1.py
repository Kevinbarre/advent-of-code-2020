import sys

answers = []
group = set()
for line in sys.stdin:
    row = line.rstrip('\n')
    # Est-ce que la ligne contient du texte ?
    if row:
        letters = {letter for letter in row}
        group.update(letters)
    else:
        answers.append(group)
        group = set()

# On ajoute le dernier
answers.append(group)

# Somme des tailles de chaque groupe
print(sum(len(group) for group in answers))


