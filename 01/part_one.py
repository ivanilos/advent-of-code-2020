

def solve(nums):
	found = set()
	for num in nums:
		if 2020 - num in found:
			return num * (2020 - num)

		found.add(num)

	return -1
	

def main():
	with open("input.txt") as input:
		nums = [int(line) for line in input.readlines()]

		ans = solve(nums)
		print(ans)

if __name__ == '__main__':
	main() 