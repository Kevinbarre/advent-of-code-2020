import re
import sys


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
my_ticket = input().split(',')

# print(my_ticket)

# Parsing des autres tickets
input()  # Ligne vide
input()  # Ligne avec "nearby tickets:"
nearby_tickets = []
for line in sys.stdin:
    nearby_tickets.append(map(int, line.rstrip('\n').split(',')))

# print(nearby_tickets)

# Vérification que les valeurs des tickets correspondent à au moins un des range
invalid_values = []
for nearby_ticket in nearby_tickets:
    for value in nearby_ticket:
        if not any(value in the_range for the_range in fields.values()):
            invalid_values.append(value)

print(sum(invalid_values))