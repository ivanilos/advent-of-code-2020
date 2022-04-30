

def solve(answers):
	answered = {}
	for ans in answers:
		for mark in ans:
			answered.setdefault(mark, 0)
			answered[mark] += 1


	
	return len([val for val in answered.values() if val == len(answers)])

	
def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()
		
		result = 0

		answers = []
		for line in lines:
			if line == '':
				result += solve(answers)
				answers = []
			else:
				answers.append(line)

		result += solve(answers)

		print(result)


if __name__ == '__main__':
	main() 