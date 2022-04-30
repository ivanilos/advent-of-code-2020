

def check(a, b, freq):
	freq[a] -= 1
	freq[b] -= 1

	if 2020 - a - b in freq and freq[2020 - a - b] > 0:
		return True

	freq[a] += 1
	freq[b] += 1
	return False

def solve(nums):
	freq = {}

	for num in nums:
		freq.setdefault(num, 0)
		freq[num] += 1

	i = 0
	while i < len(nums):
		a = nums[i]
		
		j = i + 1
		while j < len(nums):
			b = nums[j]

			if check(a, b, freq):
				return a * b * (2020 - a - b)

			j += 1

		i += 1

	return -1
	

def main():
	with open("input.txt") as input:
		nums = [int(line) for line in input.readlines()]

		ans = solve(nums)
		print(ans)

if __name__ == '__main__':
	main() 