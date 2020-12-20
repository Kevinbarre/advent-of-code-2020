import re
import sys

# Parsing des rules
from pprint import pprint

raw_rules = {}
line = input()
while line != "":
    index, rule = line.rstrip('\n').split(': ')
    raw_rules[index] = rule
    line = input()

# pprint(raw_rules)

# Parsing des messages
messages = []
for line in sys.stdin:
    messages.append(line.rstrip('\n'))

# print(messages)

rules = {}


def parse_rule(raw_rule):
    # print("Raw rule: {}".format(raw_rule))
    if '"' in raw_rule:
        # Lettre simple
        return r"" + raw_rule[1:-1]
    elif '|' not in raw_rule:
        other_rules = raw_rule.split(' ')
        results = r""
        for other_rule in other_rules:
            if other_rule not in rules:
                # On doit d'abord calculer cette règle
                rules[other_rule] = parse_rule(raw_rules[other_rule])
            results += rules[other_rule]
        # print("Final results")
        # print(results)
        return results
    else:
        sub_rules = raw_rule.split(' | ')
        return r"(" + "|".join(parse_rule(sub_rule) for sub_rule in sub_rules) + ")"


# Pour 8 et 11, on utilise la notation +
rules['8'] = parse_rule('42') + "+"
rules['11'] = parse_rule('42') + "+" + parse_rule('31') + "+"

rules['0'] = r"^" + parse_rule(raw_rules['0']) + "$"

# print("Raw rules:")
# pprint(raw_rules)
# print("Rules:")
# pprint(rules)

regex_0 = re.compile(rules['0'])

total = 0
for message in messages:
    if regex_0.fullmatch(message):
        total += 1

print(total)
