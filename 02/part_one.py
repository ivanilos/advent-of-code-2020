

def check(password, mini, maxi, target):
	qt = 0
	for ch in password:
		if ch == target:
			qt += 1

	return mini <= qt <= maxi

def solve(line):
	data = line.split()
	mini, maxi = data[0].split('-')
	char = data[1].split(':')[0]
	password = data[2]

	return check(password, int(mini), int(maxi), char)
	
def main():
	with open("input.txt") as input:
		counter = 0
		for line in input.readlines():
			counter += solve(line)

		print(counter)

if __name__ == '__main__':
	main() 