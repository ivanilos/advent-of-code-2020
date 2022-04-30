

import re

SECTIONS = 3

class BipartiteMatch:
	
	# n nodes on left
	# m nodes on right
	def __init__(self, n, m):
		self.n = n
		self.m = m
		self.match = [-1] * m
		self.g = [[] for _ in range(n)]

	def addEdge(self, a, b):
		self.g[a].append(b)

	def solve(self):
		for i in range(self.n):
			used = [False] * self.n

			self.kuhn(i, used)

		return self.match

	def kuhn(self, node, used):
		if used[node]:
			return False

		used[node] = True
		for viz in self.g[node]:
			if self.match[viz] == -1 or self.kuhn(self.match[viz], used):
				self.match[viz] = node
				return True

		return False

	def buildGraph(self, solver, validTickets, rules):
		for ruleIdx, rule in enumerate(rules):
			for namePos in range(len(validTickets[0])):
				can = True

				for ticket in validTickets:
					if not satisfy(int(ticket[namePos]), rule):
						can = False
						break

				if can:
					solver.addEdge(namePos, ruleIdx)		
		

def emptyLine(line):
	return len(line) == 0
	
def splitIntoSections(lines):
	op = 0
	sectionLines = [[] for _ in range(SECTIONS)] 

	for line in lines:
		if emptyLine(line):
			op += 1
		else:
			sectionLines[op].append(line)

	return sectionLines

def parseRules(lines):
	rules = []

	for line in lines:
		name, interval = line.split(':')
		match = re.match(r"(\d+)-(\d+) or (\d+)-(\d+)", interval.strip(), re.I)

		if match:
			items = match.groups()
			intervalA = (int(items[0]), int(items[1]))
			intervalB = (int(items[2]), int(items[3]))

			rules.append((name, intervalA, intervalB))

	return rules


def parseTickets(lines):
	return lines[1 : len(lines)]

def parse(lines):
	rulesLines, ticketLine, nearbyLines = splitIntoSections(lines)
	rules = parseRules(rulesLines)
	ticket = parseTickets(ticketLine)
	nearby = parseTickets(nearbyLines)

	return rules, ticket, nearby

def satisfy(num, rule):
	minA, maxA = rule[1][0], rule[1][1]
	minB, maxB = rule[2][0], rule[2][1]
	return minA <= num <= maxA or minB <= num <= maxB

def canBeValid(num, rules):
	for rule in rules:
		if satisfy(num, rule):
			return True

	return False
	
def isValid(ticket, rules):
	for num in ticket.split(','):
		if not canBeValid(int(num), rules):
			return False

	return True
	
def solve(myTicket, validTickets, rules):
	solver = BipartiteMatch(len(validTickets[0]), len(rules))
	solver.buildGraph(solver, validTickets, rules)
	match = solver.solve()

	result = 1
	for idx, matchedRule in enumerate(match):
		if rules[idx][0].startswith('departure'):
			result *= int(myTicket[matchedRule])

	return result


def main():
	with open("input.txt") as input:
		lines =	input.read().splitlines()

		rules, myTicket, nearby = parse(lines)
		validTickets = [ticket.split(',') for ticket in myTicket + nearby if isValid(ticket, rules)]

		ans = solve(myTicket[0].split(','), validTickets, rules)

		print(ans)
			
if __name__ == '__main__':
	main() 