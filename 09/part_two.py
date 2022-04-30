

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
	

def solvePartOne(nums):
	next = 25

	while next < len(nums):
		if not isSumOfTwo(nums[next - 25: next], nums[next]):
			return nums[next]

		next += 1


def calc(nums):
	return min(nums) + max(nums)

def solve(nums, invalid):
	prefSum = {0 : -1}

	i = 0
	curPrefSum = 0
	while i < len(nums):
		curPrefSum += nums[i]

		need = curPrefSum - invalid
		if need in prefSum:
			start = prefSum[need] + 1
			end = i + 1
			return calc(nums[start : end])

		prefSum[curPrefSum] = i

		i += 1 
	
def main():
	with open("input.txt") as input:
		lines = [int(line) for line in input.read().splitlines()]
		
		invalid = solvePartOne(lines)
		ans = solve(lines, invalid)

		print(ans)
			
if __name__ == '__main__':
	main() 