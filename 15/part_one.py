

NEED = 2020
MIN_TURNS_SPOKEN = 2

def solve(nums):
	turn = 1
	last = 0
	turnSpoken = {}

	for num in nums:
		turnSpoken.setdefault(num, [])
		turnSpoken[num].append(turn)
		last = num
		turn += 1

	while turn <= NEED:
		if len(turnSpoken[last]) >= MIN_TURNS_SPOKEN:
			diff = turnSpoken[last][-1] - turnSpoken[last][-2]

			turnSpoken.setdefault(diff, [])
			turnSpoken[diff].append(turn)
			last = diff
		else:
			turnSpoken.setdefault(0, [])
			turnSpoken[0].append(turn)
			last = 0

		turn += 1

	return last

def main():
	with open("input.txt") as input:
		nums = [int(val) for val in input.read().split(',')]
		
		ans = solve(nums)

		print(ans)
			
if __name__ == '__main__':
	main() 