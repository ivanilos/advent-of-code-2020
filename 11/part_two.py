

VACANT = 'L'
OCCUPIED = '#'

def performUpdates(seats, updates):
	for row, col, val in updates:
		seats[row][col] = val

def isVacant(row, col, seats):
	return seats[row][col] == VACANT

def isOccupied(row, col, seats):
	return seats[row][col] == OCCUPIED

def isIn(row, col, rows, cols):
	return 0 <= row < rows and 0 <= col < cols

def countOccupiedAdjacent(row, col, seats):
	occupied = 0
	rows = len(seats)
	cols = len(seats[0])

	deltaPos = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

	for deltaRow, deltaCol in deltaPos:
		step = 1
		while True:
			otherRow = row + step * deltaRow
			otherCol = col + step * deltaCol

			if isIn(otherRow, otherCol, rows, cols):
				if isOccupied(otherRow, otherCol, seats):
					occupied += 1
					break
				elif isVacant(otherRow, otherCol, seats):
					break

			else:
				break

			step += 1

	return occupied

def simulate(seats):
	updates = [(-1, -1, VACANT)]

	while len(updates) > 0:
		updates = []

		row = 0
		while row < len(seats):
			col = 0
			while col < len(seats[row]):
				occupiedAdjacent = countOccupiedAdjacent(row, col, seats)

				if isVacant(row, col, seats) and occupiedAdjacent == 0:
					updates.append((row, col, OCCUPIED))
				elif isOccupied(row, col, seats) and occupiedAdjacent >= 5:
					updates.append((row, col, VACANT))

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