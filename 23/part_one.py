

def findDestinationIdx(val, nums):
	while val not in nums:
		val -= 1

		if val <= 0:
			val = max(nums)

	return nums.index(val)

def pickCups(curIdx, cups):
	result = []

	curVal = cups[curIdx]
	for _ in range(3):
		n = len(cups)
		result.append(cups[(curIdx + 1) % n])
		del cups[(curIdx + 1) % n]

		curIdx = cups.index(curVal)

	return result, curIdx

def insertAfterDestination(cups, pickedCups, destinationIdx):
	for i, val in enumerate(pickedCups):
		cups.insert(destinationIdx + i + 1, val)

def encodeAnswer(cups):
	oneIdx = cups.index(1)
	n = len(cups)

	result = ''
	for i in range(1, n):
		result += str(cups[(oneIdx + i) % n])

	return result

def solve(cups):
	TURNS = 100

	n = len(cups)
	curIdx = 0
	curVal = cups[curIdx]
	for _ in range(TURNS):
		pickedCups, curIdx = pickCups(curIdx, cups)
		destinationIdx = findDestinationIdx(cups[curIdx] - 1, cups)
		insertAfterDestination(cups, pickedCups, destinationIdx)

		curIdx = (cups.index(curVal) + 1) % n
		curVal = cups[curIdx]

	return encodeAnswer(cups)
			
def main():
	with open("input.txt") as input:
		cups = list(map(int, input.read()))

		ans = solve(cups)

		print(ans)
			
if __name__ == '__main__':
	main() 