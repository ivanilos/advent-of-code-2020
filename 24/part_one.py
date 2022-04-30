

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

def solve(lines):
	blackTiles = set()
	
	for line in lines:
		commands = parse(line)
		x, y = tileCoordinate(commands)
		update(blackTiles, x, y)

	return len(blackTiles) 

def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()

		ans = solve(lines)

		print(ans)
			
if __name__ == '__main__':
	main() 