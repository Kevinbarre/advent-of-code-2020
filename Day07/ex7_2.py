import sys

rules = {}
for line in sys.stdin:
    parent, children = line.rstrip('\n').split("bags contain")
    # print('Parent:', parent)
    parent = parent.rstrip()
    if parent not in rules:
        rules[parent] = {}

    if children.startswith(" no other"):
        # Pas d'enfants pour ce parent
        continue

    children = children.split(',')
    for child in children:
        child = child.rstrip('.').rstrip('bags').rstrip('bag').split(maxsplit=1)
        # print('Child:', child)
        rules[parent][child[1].rstrip()] = int(child[0])


# print(rules)


def bags_number(parent_name):
    print(parent_name)
    rule = rules[parent_name]
    print(rule)
    if not rule:
        print("{} is only 1 bag".format(parent_name))
        return 1
    result = sum(rule[child_name] * bags_number(child_name) for child_name in rule) + 1
    print("{} counts for {} bags".format(parent_name, result))
    return result


# On enlève 1 car on ne compte pas le shiny gold lui même
print(bags_number("shiny gold") - 1)
