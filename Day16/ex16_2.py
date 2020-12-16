import math
import sys
from itertools import chain


def parse_range(constraints):
    ranges = constraints.split(' or ')
    result = set()
    for interval_range in ranges:
        begin, end = interval_range.split('-')
        result.update(range(int(begin), int(end) + 1))
    return result


fields = {}

# Parsing des fields
line = input()
while line != "":
    field, constraints = line.rstrip('\n').split(': ')
    fields[field] = parse_range(constraints)
    line = input()

# print(fields)

# Parsing de notre ticket
input()  # Ligne avec "your ticket:"
my_ticket = list(map(int, input().split(',')))

# print(my_ticket)

# Parsing des autres tickets
input()  # Ligne vide
input()  # Ligne avec "nearby tickets:"
nearby_tickets = []
for line in sys.stdin:
    nearby_tickets.append(list(map(int, line.rstrip('\n').split(','))))

# print(nearby_tickets)

# Vérification que les valeurs des tickets correspondent à au moins un des range
valid_nearby_tickets = []
for nearby_ticket in nearby_tickets:
    valid = True
    for value in nearby_ticket:
        if not any(value in the_range for the_range in fields.values()):
            # Ticket invalid, on ne le garde pas
            valid = False
            break
    # Si le ticket a passé tous les contrôles, on le garde
    if valid:
        valid_nearby_tickets.append(list(nearby_ticket))

# print(valid_nearby_tickets)

# On calcule les valeurs discriminatoires de chaque champ
fields_impossible_values = {}

for field, field_values in fields.items():
    # print("{} values: {}".format(field, field_values))
    other_fields_values = set(chain.from_iterable(
        other_field_values for other_field, other_field_values in fields.items() if other_field != field))
    # print("Other fields values: {}".format(other_fields_values))
    impossible_values = other_fields_values.difference(field_values)
    # print("Impossible {} values: {}".format(field, impossible_values))
    fields_impossible_values[field] = impossible_values

# print(fields_impossible_values)
possible_choices = {field: set(range(0, len(fields))) for field in fields}

# Pour chaque ticket
for nearby_ticket in valid_nearby_tickets:
    # Pour chaque valeur dans le ticket
    for i, value in enumerate(nearby_ticket):
        # Pour chaque champ
        for field, impossible_values in fields_impossible_values.items():
            # On vérifie si la valeur est impossible pour ce champ
            if value in impossible_values:
                # Alors la position n'est pas possible pour ce champ
                possible_choices[field].discard(i)

field_positions = ["" for field in fields]
while possible_choices:
    # On distingue les champs pour lequels une seule valeur est encore possible, des autres à traiter plus tard
    single_choices, next_possible_choices = {}, {}
    for k, v in possible_choices.items():
        if len(v) == 1:
            single_choices[k] = v.pop()
        else:
            next_possible_choices[k] = v
    # print(single_choices)
    # print(next_possible_choices)
    for field, position in single_choices.items():
        field_positions[position] = field
        # On enlève cette position dans ceux restants
        for _, remaining_positions in next_possible_choices.items():
            remaining_positions.discard(position)
    possible_choices = next_possible_choices

# print(field_positions)

result = []
for i, field in enumerate(field_positions):
    if field.startswith("departure"):
        result.append(my_ticket[i])

print(math.prod(result))
