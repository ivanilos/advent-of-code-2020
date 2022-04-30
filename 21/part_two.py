

import re
from itertools import permutations

def parse(lines):
	food = []

	for line in lines:
		match = re.match(r"([\w+ ]+) \(contains (.+)\)", line, re.I)
		if match:
			items = match.groups()
			ingredients = items[0].split()
			allergens = [val.strip() for val in items[1].split(',')]
			food.append([ingredients, allergens])

	return food
		
def possibleAllergensToIngredients(food):
	allergenToIngredient = {}

	for ingredients, allergens in food:
		for allergen in allergens:
			possibleIngredients = set()
			for ingredient in ingredients:
				possibleIngredients.add(ingredient)

			if allergen in allergenToIngredient:
				allergenToIngredient[allergen] = allergenToIngredient[allergen].intersection(possibleIngredients)
			else:
				allergenToIngredient[allergen] = possibleIngredients

	return allergenToIngredient

def check(ingredients, allergens, allergenToIngredient):
	for idx, ingredient in enumerate(ingredients):
		if ingredient not in allergenToIngredient[allergens[idx]]:
			return False

	return True

def discoverIngredientAllergen(allergenToIngredient):
	allergens = sorted([key for key in allergenToIngredient.keys()])
	ingredients = set()
	for ingredient in allergenToIngredient.values():
		ingredients = ingredients.union(ingredient)

	ingredients = list(ingredients)
	
	generatedPerms = permutations(ingredients) 
	for perm in list(generatedPerms):
		if check(perm, allergens, allergenToIngredient):
			return ','.join(perm)
	

def solve(lines):
	food = parse(lines)

	allergenToIngredient = possibleAllergensToIngredients(food)

	ans = discoverIngredientAllergen(allergenToIngredient)

	return ans

def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()

		ans = solve(lines)

		print(ans)
			
if __name__ == '__main__':
	main() 