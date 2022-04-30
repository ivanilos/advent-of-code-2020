

from collections import deque

def isEmpty(line):
	return len(line) == 0

def splitIntoSections(lines):
	SECTIONS = 2
	op = 0
	sectionLines = [[] for _ in range(SECTIONS)] 

	for line in lines:
		if isEmpty(line):
			op += 1
		else:
			sectionLines[op].append(line)

	return sectionLines
			
			
def parse(lines):
	player1, player2 = splitIntoSections(lines)
	player1 = deque(map(int, player1[1 : len(player1)]))
	player2 = deque(map(int, player2[1 : len(player2)]))

	return player1, player2

def score(player):
	result = 0
	for idx, val in enumerate(player):
		result += (len(player) - idx) *  val

	return result

def isGameOver(player1, player2):
	return len(player1) == 0 or len(player2) == 0

def nextTurn(player1, player2):
	a, b = player1.popleft(), player2.popleft()

	if a > b:
		player1.append(a)
		player1.append(b)
	else:
		player2.append(b)
		player2.append(a)

def solve(lines):
	player1, player2 = parse(lines)

	while not isGameOver(player1, player2):
		nextTurn(player1, player2)

	return max(score(player1), score(player2))

def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()

		ans = solve(lines)

		print(ans)
			
if __name__ == '__main__':
	main() 