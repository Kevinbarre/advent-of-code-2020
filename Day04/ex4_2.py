import re
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
    if all(k in passport for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
        return check_valid_byr(passport["byr"]) and check_valid_iyr(passport["iyr"]) and check_valid_eyr(
            passport["eyr"]) and check_valid_hgt(passport["hgt"]) and check_valid_hcl(
            passport["hcl"]) and check_valid_ecl(passport["ecl"]) and check_valid_pid(passport["pid"])
    else:
        return False


def check_valid_byr(byr):
    return 1920 <= int(byr) <= 2002


def check_valid_iyr(iyr):
    return 2010 <= int(iyr) <= 2020


def check_valid_eyr(eyr):
    return 2020 <= int(eyr) <= 2030


def check_valid_hgt(hgt):
    size, unit = hgt[:-2], hgt[-2:]
    if unit == "cm":
        return 150 <= int(size) <= 193
    elif unit == "in":
        return 59 <= int(size) <= 76
    else:
        return False


def check_valid_hcl(hcl):
    if hcl[0] != '#':
        return False
    return re.match(r'[a-f0-9]{6}', hcl[1:])


def check_valid_ecl(ecl):
    return ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def check_valid_pid(pid):
    return len(pid) == 9 and pid.isdigit()


total = 0
for passport in entries:
    if check_valid(passport):
        total += 1

print(total)
