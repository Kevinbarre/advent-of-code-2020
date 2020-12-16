import re
import sys
from collections import Counter


class Policy:
    def __init__(self, minimum, maximum, letter, password):
        self.minimum = minimum
        self.maximum = maximum
        self.letter = letter
        self.password = password

    def __repr__(self):
        return 'Min: {}, Max: {}, Letter:  {}, Password: {}'.format(self.minimum, self.maximum, self.letter,
                                                                    self.password)


policies = []
for line in sys.stdin:
    # Séparation selon les tokens '-', ' ' et ':'
    splits = re.split(r'[- :]', line.rstrip('\n'))
    # Création d'un objet Policy correspondant
    # On ignore l'index 3 qui contient une chaîne vide
    policies.append(Policy(int(splits[0]), int(splits[1]), splits[2], splits[4]))

# print(policies)
total = 0

for policy in policies:
    # On compte le nombre d'occurence de la lettre
    counter = Counter(policy.password).get(policy.letter, 0)
    # On vérifie si elle est bien située entre le min et le max
    if policy.minimum <= counter <= policy.maximum:
        total += 1

print(total)
