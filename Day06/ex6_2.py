import sys

answers = []
group = []
for line in sys.stdin:
    row = line.rstrip('\n')
    # Est-ce que la ligne contient du texte ?
    if row:
        # Nouvelle personne dans le groupe
        person = {letter for letter in row}
        group.append(person)
    else:
        # Nouveau groupe
        answers.append(group)
        group = []

# On ajoute le dernier
answers.append(group)

# Intersection des réponses de chaque groupe
result = [set.intersection(*group) for group in answers]

# Somme des tailles de chaque intersection
print(sum(len(intersection) for intersection in result))


