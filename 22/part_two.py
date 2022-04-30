

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
	player1 = player1[1 : len(player1)]
	player2 = player2[1 : len(player2)]

	return player1, player2

def score(player):
	result = 0
	for idx, val in enumerate(player):
		result += (len(player) - idx) *  int(val)

	return result

def isGameOver(player1, player2, reachedStates):
	state = (''.join(player1), ''.join(player2))
	return state in reachedStates or len(player1) == 0 or len(player2) == 0

def nextTurn(player1, player2):
	a, b = player1.pop(0), player2.pop(0)

	if len(player1) >= int(a) and len(player2) >= int(b):
		winner, cards = RecursiveCombat(player1[0 : int(a)], player2[0 : int(b)])
	else:
		winner = 'player1' if int(a) > int(b) else 'player2'

	if winner == 'player1':
		player1.append(a)
		player1.append(b)
	else:
		player2.append(b)
		player2.append(a)

def firstPlayerWin(player1, player2, reachedStates):
	state = (''.join(player1), ''.join(player2))
	return len(player2) == 0 or state in reachedStates
	
def RecursiveCombat(player1, player2):
	reachedStates = set()
	while not isGameOver(player1, player2, reachedStates):
		nextState = (''.join(player1), ''.join(player2))
		reachedStates.add(nextState)
		nextTurn(player1, player2)

	winnerTuple = ('player1', player1) if firstPlayerWin(player1, player2, reachedStates) else ('player2', player2)

	return winnerTuple
	
def solve(lines):
	player1, player2 = parse(lines)

	winner, cards = RecursiveCombat(player1, player2)

	return score(cards)

def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()

		ans = solve(lines)

		print(ans)
			
if __name__ == '__main__':
	main() 