

import re

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

def solve(lines):
	food = parse(lines)

	allergenToIngredient = possibleAllergensToIngredients(food)
	
	possibleAllergicIngredients = set()

	for ingredients in allergenToIngredient.values():
		possibleAllergicIngredients = possibleAllergicIngredients.union(ingredients)

	ans = 0
	for ingredients, _ in food:
		for ingredient in ingredients:
			if ingredient not in possibleAllergicIngredients:
				ans += 1

	return ans

def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()

		ans = solve(lines)

		print(ans)
			
if __name__ == '__main__':
	main() 