

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
	
def main():
	with open("input.txt") as input:

		ans = 0

		for line in input.read().splitlines():
			ans = max(ans, passID(line))

		print(ans)


if __name__ == '__main__':
	main() 