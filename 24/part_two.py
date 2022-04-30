

import re

def parse(line):
	match = re.split('(ne|nw|w|se|sw|e)', line)
	return list(filter(('').__ne__, match))

def tileCoordinate(commands):
	moves = {'ne' : (0, 1), 'nw' : (-1, 1), 'w' : (-1, 0),
				'se' : (1, -1), 'sw' : (0, -1), 'e' : (1, 0)}

	x, y = 0, 0
	for command in commands:
		x += moves[command][0]
		y += moves[command][1]

	return x, y

def update(blackTiles, x, y):
	if (x, y) in blackTiles:
		blackTiles.remove((x, y))
	else:
		blackTiles.add((x, y))

def addAdjacent(tile, blackAdjacentCount):
	adjacentDelta = [(0, 1), (-1, 1), (-1, 0), (1, -1), (0, -1), (1, 0)]

	for delta in adjacentDelta:
		x, y = tile[0] + delta[0], tile[1] + delta[1]
		blackAdjacentCount.setdefault((x, y), 0)
		blackAdjacentCount[(x, y)] += 1

def gameOfLifeTurn(blackTiles):
	blackAdjacentCount = {}

	for tile in blackTiles:
		blackAdjacentCount.setdefault(tile, 0)
		addAdjacent(tile, blackAdjacentCount)

	newBlackTiles = set()
	for tile, count in blackAdjacentCount.items():
		if tile in blackTiles and count != 0 and count <= 2:
			newBlackTiles.add(tile)
		elif tile not in blackTiles and count == 2:
			newBlackTiles.add(tile)

	return newBlackTiles

def initialBlackTiles(lines):
	blackTiles = set()
	
	for line in lines:
		commands = parse(line)
		x, y = tileCoordinate(commands)
		update(blackTiles, x, y)

	return blackTiles

def solve(lines):
	blackTiles = initialBlackTiles(lines)

	TURNS = 100
	for _ in range(TURNS):
		blackTiles = gameOfLifeTurn(blackTiles)

	return len(blackTiles)

def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()

		ans = solve(lines)

		print(ans)
			
if __name__ == '__main__':
	main() 