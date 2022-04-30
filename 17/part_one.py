

def isActive(block):
	return block == '#'

def activeBlocksSet(blocks):
	active = set()

	for x, blockLine in enumerate(blocks):
		for y, block in enumerate(blockLine):
			if isActive(block):
				active.add((x, y, 0))

	return active

def activeNeighboursQuantity(active):
	activeNeighbours = {}

	for x, y, z in active:
		for i in range(-1, 2, 1):
			for j in range(-1, 2, 1):
				for k in range(-1, 2, 1):
					nx = x + i
					ny = y + j
					nz = z + k
					if not (nx == x and ny == y and nz == z):
						activeNeighbours.setdefault((nx, ny, nz), 0)
						activeNeighbours[(nx, ny, nz)] += 1

	return activeNeighbours

def calcNextActives(active, activeNeighbours):
	nextActive = set()

	for (x, y, z), val in activeNeighbours.items():
		if (x, y, z) in active and val in [2, 3]:
			nextActive.add((x, y, z))
		elif (x, y, z) not in active and val == 3:
			nextActive.add((x, y, z))

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