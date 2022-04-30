

dpDFS = {}
dpComply = {}

def emptyLine(line):
	return len(line) == 0

def splitIntoSections(lines):
	op = 0
	SECTIONS = 2
	sectionLines = [[] for _ in range(SECTIONS)] 

	for line in lines:
		if emptyLine(line):
			op += 1
		else:
			sectionLines[op].append(line)

	return sectionLines

def parseRules(rulesLines):
	rules = {}

	for line in rulesLines:
		leftSide, rightSide = line.split(':')
		val = [val.split() for val in rightSide.strip().split('|')]
		rules[leftSide] = val

	return rules
		
def parse(lines):
	rulesLines, strings = splitIntoSections(lines)
	rules = parseRules(rulesLines)

	return rules, strings

def comply(string, rules, curRule, idx, next):
	if (string, curRule, idx, next) in dpComply:
		return dpComply[(string, curRule, idx, next)]

	result = rules[curRule][idx]

	if next >= len(result):
		return len(string) == 0
	elif result[next] in ["a", "b"]:
		return string[0] == result[next] and comply(string[1 : len(string)], rules, curRule, idx, next + 1)

	can = False
	for sz in range(len(string)):
		left = string[0 : sz + 1]
		right = string[sz + 1 : len(string)]
		can |= DFS(left, rules, result[next]) and comply(right, rules, curRule, idx, next + 1)

	dpComply[(string, curRule, idx, next)] = can
	return can

def DFS(string, rules, curRule):
	if (string, curRule) in dpDFS:
		return dpDFS[(string, curRule)]

	results = rules[curRule]

	can = False
	for idx, result in enumerate(results):
		can |= comply(string, rules, curRule, idx, 0)
			
	dpDFS[(string, curRule)] = can
	return can

def satisfy(string, rules):
	return DFS(string, rules, '0')

def updateRulesForPartTwo(rules):
	rules["8"] = [['42'], ['42', '8']]
	rules["11"] = [['42', '31'], ['42', '11', '31']]

def solve(lines):
	rules, strings = parse(lines)
	updateRulesForPartTwo(rules)

	ans = 0
	for string in strings:
		ans += satisfy(string, rules)

	return ans

def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()

		ans = solve(lines)

		print(ans)
			
if __name__ == '__main__':
	main() 