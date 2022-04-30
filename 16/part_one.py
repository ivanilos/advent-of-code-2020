

import re

SECTIONS = 3

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

def canBeValid(num, rules):
	for rule in rules:
		minA, maxA = rule[1][0], rule[1][1]
		minB, maxB = rule[2][0], rule[2][1]

		if minA <= num <= maxA or minB <= num <= maxB:
			return True

	return False
		
def solve(rules, tickets):
	result = 0

	for ticket in tickets:
		for num in ticket.split(','):
			if not canBeValid(int(num), rules):
				result += int(num)

	return result
				

def main():
	with open("input.txt") as input:
		lines =	input.read().splitlines()

		rules, ticket, nearby = parse(lines)

		ans = solve(rules, nearby)

		print(ans)
			
if __name__ == '__main__':
	main() 