

def isSumOfTwo(nums, target):
	idxA = 0
	while idxA < len(nums):
		idxB = idxA + 1
		while idxB < len(nums):
			if nums[idxA] + nums[idxB] == target:
				return True

			idxB += 1

		idxA += 1

	return False
	

def solve(nums):
	next = 25

	while next < len(nums):
		if not isSumOfTwo(nums[next - 25: next], nums[next]):
			return nums[next]

		next += 1
	
	
def main():
	with open("input.txt") as input:
		lines = [int(line) for line in input.read().splitlines()]
		
		ans = solve(lines)
		print(ans)
			
if __name__ == '__main__':
	main() 