

import re

class Rules:

	def __init__(self):
		self.colors = []
		self.rules = {}

	def addRule(self, container, inside):
		self.rules.setdefault(container, [])
		self.rules[container].append(inside)

	def parse(self, line):
		leftSide, rightSide = line.split('contain')
		rightSide = rightSide.split(',')

		_, leftColor = self.color(leftSide)
		self.colors.append(leftColor)

		for bagPhrase in rightSide:
			rightQuantityAndColor = self.color(bagPhrase.strip())
			self.addRule(leftColor, rightQuantityAndColor)


	def color(self, bagPhrase):
		match = re.match(r"(\d )*(\w+ \w+)", bagPhrase, re.I)
		if match:
			items = match.groups()
			qt = items[0] if items[0] != None else 1

			return qt, items[1]

		return ""
		

	def solve(self, startBag):
		counted = {}
		ans = self.DFS(startBag, counted)	

		return ans

	def DFS(self, color, counted):
		if color in counted:
			return counted[color]
		elif color == "no other":
			return 0

		counted[color] = 1

		for quantity, bag in self.rules[color]:
			counted[color] += int(quantity) * self.DFS(bag, counted)

		return counted[color]
		
	
def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()

		bagRules = Rules()

		for line in lines:
			bagRules.parse(line)

		ans = bagRules.solve("shiny gold")

		print(ans - 1) # subtract from golden bag itself
			
if __name__ == '__main__':
	main() 