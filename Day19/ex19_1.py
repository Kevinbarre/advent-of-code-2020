import sys

# Parsing des rules
raw_rules = {}
line = input()
while line != "":
    index, rule = line.rstrip('\n').split(': ')
    raw_rules[index] = rule
    line = input()

# print(raw_rules)

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
        return {raw_rule[1:-1]}
    elif '|' not in raw_rule:
        other_rules = raw_rule.split(' ')
        results = {''}
        for other_rule in other_rules:
            if other_rule not in rules:
                # On doit d'abord calculer cette règle
                rules[other_rule] = parse_rule(raw_rules[other_rule])
            results = {result + other for result in results for other in rules[other_rule]}
        # print("Final results")
        # print(results)
        return results
    else:
        sub_rules = raw_rule.split(' | ')
        return {elem for sub_rule in sub_rules for elem in parse_rule(sub_rule)}


rule_0 = parse_rule(raw_rules['0'])

# print(rule_0)

total = 0
for message in messages:
    if message in rule_0:
        total += 1

print(total)
