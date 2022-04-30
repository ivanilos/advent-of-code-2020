

def solve(passport):
	needed_attr = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

	got = set()
	for line in passport:
		data = line.split()
		for attr in data:
			got.add(attr.split(':')[0])

	for needed in needed_attr:
		if needed not in got:
			return False

	return True
		
	
def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()
		
		ans = 0

		passport = []
		for line in lines:
			if line == '':
				ans += solve(passport)
				passport = []
			else:
				passport.append(line)

		ans += solve(passport)

		print(ans)

if __name__ == '__main__':
	main() 