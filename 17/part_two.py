

def isActive(block):
	return block == '#'

def activeBlocksSet(blocks):
	active = set()

	for x, blockLine in enumerate(blocks):
		for y, block in enumerate(blockLine):
			if isActive(block):
				active.add((x, y, 0, 0))

	return active

def activeNeighboursQuantity(active):
	activeNeighbours = {}

	for x, y, z, w in active:
		for i in range(-1, 2, 1):
			for j in range(-1, 2, 1):
				for k in range(-1, 2, 1):
					for p in range(-1, 2, 1):
						nx = x + i
						ny = y + j
						nz = z + k
						nw = w + p
						if not (nx == x and ny == y and nz == z and nw == w):
							activeNeighbours.setdefault((nx, ny, nz, nw), 0)
							activeNeighbours[(nx, ny, nz, nw)] += 1

	return activeNeighbours

def calcNextActives(active, activeNeighbours):
	nextActive = set()

	for (x, y, z, w), val in activeNeighbours.items():
		if (x, y, z, w) in active and val in [2, 3]:
			nextActive.add((x, y, z, w))
		elif (x, y, z, w) not in active and val == 3:
			nextActive.add((x, y, z, w))

	return nextActive
	
def solve(blocks):
	TIMER = 6
	
	active = activeBlocksSet(blocks)
	for timer in range(TIMER):
		activeNeighbours = activeNeighboursQuantity(active)
		active = calcNextActives(active, activeNeighbours)

	return len(active)

def main():
	with open("input.txt") as input:
		blocks = input.read().splitlines()

		ans = solve(blocks)

		print(ans)
			
if __name__ == '__main__':
	main() 