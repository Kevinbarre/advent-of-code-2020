import sys

entries = []
entry = {}
for line in sys.stdin:
    row = line.rstrip('\n')
    # Est-ce que la ligne contient du texte ?
    if row:
        key_values = {k: v for k, v in map(lambda elem: elem.split(':'), row.split())}
        entry.update(key_values)
    else:
        entries.append(entry)
        entry = {}

# On ajoute le dernier
entries.append(entry)


def check_valid(passport):
    # Tous les champs sauf "cip" sont obligatoires
    return all(k in passport for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))


total = 0
for passport in entries:
    if check_valid(passport):
        total += 1

print(total)
