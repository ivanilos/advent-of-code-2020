

def calc(adapterIdx, lastVoltage, adaptersVolts, memo):
	if (adapterIdx, lastVoltage) in memo:
		return memo[(adapterIdx, lastVoltage)]

	if adapterIdx >= len(adaptersVolts):
		return lastVoltage == adaptersVolts[-1]
	
	# dont put the adapter
	ways = calc(adapterIdx + 1, lastVoltage, adaptersVolts, memo)
	# put the adapter
	if adaptersVolts[adapterIdx] - lastVoltage <= 3:
		ways += calc(adapterIdx + 1, adaptersVolts[adapterIdx], adaptersVolts, memo)

	memo[(adapterIdx, lastVoltage)] = ways
	return ways


def solve(adaptersVolts):
	adaptersVolts.sort()

	memo = {}
	ways = calc(0, 0, adaptersVolts, memo)
	return ways
	
def main():
	with open("input.txt") as input:
		lines = [int(line) for line in input.read().splitlines()]

		ans = solve(lines)

		print(ans)
			
if __name__ == '__main__':
	main() 