

def count(down, right, lines, rows, cols):
	ans = 0

	row = 0
	while row + 1 < rows:
		row += down
		col = ((row // down) * right) % cols

		if lines[row][col] == '#':
			ans += 1

	return ans

def solve(lines):
	rows = len(lines)
	cols = len(lines[0])

	slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

	ans = 1
	for slope in slopes:
		ans *= count(slope[0], slope[1], lines, rows, cols)

	return ans
	
def main():
	with open("input.txt") as input:
		ans = solve(input.read().splitlines())
		print(ans)

if __name__ == '__main__':
	main() 