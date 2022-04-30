

def calc(val):
	pos = 0

	for ch in val:
		pos *= 2
		if ch in ['B', 'R']:
			pos += 1

	return pos

def passID(boardPass):
	row = calc(boardPass[0:7])
	col = calc(boardPass[7:])

	return row * 8 + col
	

def solve(occupiedSeats):
	for seat in occupiedSeats:
		if seat + 1 not in occupiedSeats and seat + 2 in occupiedSeats:
			return seat + 1

	return -1

def main():
	with open("input.txt") as input:

		found = set()

		for line in input.read().splitlines():
			seatID = passID(line)
			found.add(seatID)

		ans = solve(found)

		print(ans)


if __name__ == '__main__':
	main() 