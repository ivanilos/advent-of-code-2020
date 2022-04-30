

def solve(waitTime, buses):
	minWait = waitTime
	busIDforMinWait = 0

	for bus in buses:
		wait = (bus - waitTime % bus) % bus

		if wait < minWait:
			minWait = wait
			busIDforMinWait = bus

	return minWait * busIDforMinWait
	
def main():
	with open("input.txt") as input:
		waitTime = int(input.readline())
		buses = [int(bus) for bus in input.readline().split(',') if bus != 'x']

		ans = solve(waitTime, buses)

		print(ans)
			
if __name__ == '__main__':
	main() 