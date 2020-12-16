import re
import sys


class Policy:
    def __init__(self, first, second, letter, password):
        self.first = first
        self.second = second
        self.letter = letter
        self.password = password

    def __repr__(self):
        return 'First: {}, Second: {}, Letter:  {}, Password: {}'.format(self.first, self.second, self.letter,
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
    # On récupère les lettres aux bonnes positions (décalage d'index de 1)
    first_letter = policy.password[policy.first - 1]
    second_letter = policy.password[policy.second - 1]
    # On vérifie qu'uniquement une des deux correspond à la lettre attendue (ou exclusif)
    if (first_letter == policy.letter) ^ (second_letter == policy.letter):
        total += 1

print(total)
