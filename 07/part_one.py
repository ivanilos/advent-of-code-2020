

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

		leftColor = self.color(leftSide)
		self.colors.append(leftColor)

		for bagPhrase in rightSide:
			rightColor = self.color(bagPhrase.strip())
			self.addRule(leftColor, rightColor)


	def color(self, bagPhrase):
		match = re.match(r"[\d ]*(\w+ \w+)", bagPhrase, re.I)
		if match:
			items = match.groups()
			return items[0]

		return ""
		

	def solve(self, endBag):
		can = {}
		ans = 0		

		for color in self.colors:
			ans += self.DFS(color, endBag, can)

		return ans

	def DFS(self, color, endBag, can):
		if color in can:
			return can[color]
		elif color == endBag:
			return 1
		elif color == "no other":
			return 0

		can[color] = 0

		for bag in self.rules[color]:
			can[color] |= self.DFS(bag, endBag, can)

		return can[color]
		
	
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