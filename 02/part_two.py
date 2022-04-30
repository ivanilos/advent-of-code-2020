

def check(password, posA, posB, target):
	return (password[posA] == target) ^ (password[posB] == target)

def solve(line):
	data = line.split()
	posA, posB = data[0].split('-')
	char = data[1].split(':')[0]
	password = data[2]

	return check(password, int(posA) - 1, int(posB) - 1, char)
	
def main():
	with open("input.txt") as input:
		counter = 0
		for line in input.readlines():
			counter += solve(line)

		print(counter)

if __name__ == '__main__':
	main() 