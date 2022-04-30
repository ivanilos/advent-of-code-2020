

import re

def byr(val):
	return 1920 <= int(val) <= 2002

def iyr(val):
	return 2010 <= int(val) <= 2020

def eyr(val):
	return 2020 <= int(val) <= 2030

def hgt(val):
	match = re.match(r"(\d+)(\w+)", val, re.I)
	if match:
		items = match.groups()

		if items[1] == 'cm':
			return 150 <= int(items[0]) <= 193
		elif items[1] == 'in':
			return 59 <= int(items[0]) <= 76	

	return False

def hcl(val):
	match = re.match(r"#([0-9a-f]){6}", val, re.I)
	if match:
		return True

	return False

def ecl(val):
	return val in ['amb', 'blu', 'brn', 'gry', 'grn',
					'hzl', 'oth']

def pid(val):
	return len(val) == 9 and val.isdecimal()
	

def solve(passport):
	needed_attr = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	checker = {'byr': byr, 'iyr': iyr, 'eyr': eyr, 'hgt': hgt, 
				'hcl': hcl, 'ecl': ecl, 'pid': pid}

	got = {}
	for line in passport:
		data = line.split()
		for attr in data:
			key, val = attr.split(':')
			got[key] = val

	for needed in needed_attr:
		if needed not in got or not checker[needed](got[needed]):
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