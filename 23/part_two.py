

class Cups:
	def __init__(self, inputCups):
		CUPS = 10 ** 6
		self.maxVal = CUPS
		self.cups = [i for i in range(0, CUPS + 1)]
		self.next = [(i + 1) % (CUPS + 1) for i in range(0, CUPS + 1)]

		for idx, val in enumerate(inputCups):
			if idx + 1 < len(inputCups):
				self.next[val] = inputCups[idx + 1]
			else:
				self.next[val] = idx + 2

		self.curIdx = inputCups[0]
		self.next[-1] = inputCups[0]

	def pick(self):
		QUANTITY = 3
		result = []

		curVal = self.curIdx
		for _ in range(QUANTITY):
			result.append(self.next[curVal])
			curVal = self.next[curVal]

		return result

	def findDestination(self, picked):
		val = self.curIdx - 1
		while val in picked or val <= 0:
			if val <= 0:
				val = self.maxVal
			else:
				val -= 1

		return val

	def insertAfter(self, destination, picked):
		self.next[self.curIdx] = self.next[picked[-1]]

		self.next[picked[-1]] = self.next[destination]
		self.next[destination] = picked[0]

	def selectNextCup(self):
		self.curIdx = self.next[self.curIdx]
		

	def encodeAnswer(self):
		result = self.next[1] * self.next[self.next[1]]

		return result

def solve(inputCups):
	TURNS = 10 * 10**6

	cups = Cups(inputCups)

	for _ in range(TURNS):
		picked = cups.pick()
		destination = cups.findDestination(picked)
		cups.insertAfter(destination, picked)
		cups.selectNextCup()

	return cups.encodeAnswer()
			
def main():
	with open("input.txt") as input:
		inputCups = list(map(int, input.read()))

		ans = solve(inputCups)

		print(ans)
			
if __name__ == '__main__':
	main() 