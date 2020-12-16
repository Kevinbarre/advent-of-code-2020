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
        rules[parent][child[1].rstrip()] = child[0]

# print(rules)

searched_bags = []
matching_bags = {"shiny gold"}
total = 0
while matching_bags:
    print("Begging of loop. Matching bags is:", matching_bags)
    # On prépare la liste des parents à vérifier au prochain coup
    next_matching_bags = set()
    for parent, children in rules.items():
        # print("Parent", parent)
        # print("Children", children)
        # Si au moins un des sacs que l'on cherche est inclus dans ce parent, et que ce parent n'a pas déjà été identifié comme un sac candidat
        if parent not in searched_bags and parent not in matching_bags and any(
                child in children for child in matching_bags):
            print("Found a matching bag ! Will search for {} next".format(parent))
            total += 1
            # On devra vérifier qui contient le parent au prochain coup
            next_matching_bags.add(parent)
    searched_bags.extend(matching_bags)
    matching_bags = next_matching_bags

print(sorted(searched_bags))
print(total)
