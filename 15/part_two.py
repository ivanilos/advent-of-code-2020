

NEED = 30000000
MIN_TURNS_SPOKEN = 2

def recordTurnSpoken(mapa, key, val):
	mapa.setdefault(key, [])
	
	aux = mapa[key]
	if len(aux) >= MIN_TURNS_SPOKEN:
		mapa[key][-2] = mapa[key][-1]
		mapa[key][-1] = val
	else:
		mapa[key].append(val)

def solve(nums):
	turn = 1
	last = 0
	turnSpoken = {}

	for num in nums:
		recordTurnSpoken(turnSpoken, num, turn)
		last = num
		turn += 1

	while turn <= NEED:
		if len(turnSpoken[last]) >= MIN_TURNS_SPOKEN:
			diff = turnSpoken[last][-1] - turnSpoken[last][-2]

			recordTurnSpoken(turnSpoken, diff, turn)
			last = diff
		else:
			recordTurnSpoken(turnSpoken, 0, turn)
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