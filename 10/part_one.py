

def solve(adaptersVolts):
	adaptersVolts.sort()

	curVoltage = 0
	diffVolt = [0] * 4
	for volt in adaptersVolts:
		delta = volt - curVoltage
		diffVolt[delta] += 1
		
		curVoltage = volt

	return diffVolt[1] * (diffVolt[3] + 1)

	
def main():
	with open("input.txt") as input:
		lines = [int(line) for line in input.read().splitlines()]

		ans = solve(lines)

		print(ans)
			
if __name__ == '__main__':
	main() 