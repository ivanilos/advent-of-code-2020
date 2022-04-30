

EMPTY = 'L'
OCCUPIED = '#'

def performUpdates(seats, updates):
	for row, col, val in updates:
		seats[row][col] = val

def isEmpty(row, col, seats):
	return seats[row][col] == 'L'

def isOccupied(row, col, seats):
	return seats[row][col] == '#'

def isIn(row, col, rows, cols):
	return 0 <= row < rows and 0 <= col < cols

def countOccupiedAdjacent(row, col, seats):
	occupied = 0
	rows = len(seats)
	cols = len(seats[0])

	deltaPos = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

	for deltaRow, deltaCol in deltaPos:
		otherRow = row + deltaRow
		otherCol = col + deltaCol

		if isIn(otherRow, otherCol, rows, cols) and isOccupied(otherRow, otherCol, seats):
			occupied += 1

	return occupied

def simulate(seats):
	updates = [(-1, -1, EMPTY)]

	while len(updates) > 0:
		updates = []

		row = 0
		while row < len(seats):
			col = 0
			while col < len(seats[row]):
				occupiedAdjacent = countOccupiedAdjacent(row, col, seats)

				if isEmpty(row, col, seats) and occupiedAdjacent == 0:
					updates.append((row, col, OCCUPIED))
				elif isOccupied(row, col, seats) and occupiedAdjacent >= 4:
					updates.append((row, col, EMPTY))

				col += 1

			row += 1

		performUpdates(seats, updates)

def solve(seats):
	simulate(seats)

	ans = 0
	for row in seats:
		for seat in row:
			ans += seat == '#'

	return ans
	
	
def main():
	with open("input.txt") as input:
		seats = [list(line) for line in input.read().splitlines()]

		ans = solve(seats)

		print(ans)
			
if __name__ == '__main__':
	main() 