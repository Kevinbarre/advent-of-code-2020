import copy
import math
import sys
from itertools import combinations

foods = []
for line in sys.stdin:
    row = line.rstrip('\n')
    # Est-ce qu'il y a des allergènes listés ?
    if "contains" in row:
        raw_ingredients, raw_allergens = row.split(" (contains ")
        raw_ingredients = raw_ingredients.split(" ")
        raw_allergens = raw_allergens[:-1].split(", ")
    else:
        raw_ingredients = row.split(" ")
        raw_allergens = []
    # On référence une food avec ses allergènes
    foods.append((raw_ingredients, raw_allergens))

# print(foods)

# Dict des allergènes et les ingrédients qui peuvent les contenir
allergens = {}
for food_ingredients, food_allergens in foods:
    for food_allergen in food_allergens:
        if food_allergen in allergens:
            # Allergène connu, on élimine tous les ingrédients potentiels qui ne sont pas présents dans les ingrédients
            allergens[food_allergen].intersection_update(food_ingredients)
        else:
            # Nouvel allergène, tous les ingrédients peuvent le contenir
            allergens[food_allergen] = {food_ingredient for food_ingredient in food_ingredients}

# On reboucle sur les allergènes jusqu'à ce qu'on ait l'ingrédient pour chacun
while any(len(v) != 1 for v in allergens.values()):
    # Dict des ingrédients dont on est certain de l'allergène
    ingredients_with_allergen_identified = {next(iter(ingredients)) for _, ingredients in allergens.items() if
                                            len(ingredients) == 1}
    for allergen, ingredients in allergens.items():
        if len(ingredients) != 1:
            ingredients.difference_update(ingredients_with_allergen_identified)

print(",".join(value.pop() for key, value in sorted(allergens.items())))
