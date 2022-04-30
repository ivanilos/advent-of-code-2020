

def solve(lines):
	rows = len(lines)
	cols = len(lines[0])

	ans = 0

	row = 0
	while row + 1 < rows:
		row += 1
		col = (row * 3) % cols

		if lines[row][col] == '#':
			ans += 1

	return ans
	
def main():
	with open("input.txt") as input:
		ans = solve(input.read().splitlines())
		print(ans)

if __name__ == '__main__':
	main() 