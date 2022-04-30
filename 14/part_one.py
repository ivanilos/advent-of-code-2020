
	
MASK_OP = 0
MEM_OP = 1

def parse(line):
	left, right = line.split('=')
	left = left.strip()
	right = right.strip()

	if left[0 : 3] == 'mem':
		return (MEM_OP, left[4 : len(left) - 1], int(right))
	else:
		return (MASK_OP, right)

def calc(mask, val):
	bitPos = 35

	for bit in mask:
		if bit == '1':
			val |= 1 << bitPos
		elif bit == '0':
			val &= ~(1 << bitPos)

		bitPos -= 1

	return val

def solve(ops):
	mem = {}
	mask = 0

	for op in ops:
		if op[0] == MASK_OP:
			mask = op[1]
		elif op[0] == MEM_OP:
			mem[op[1]] = calc(mask, op[2])

	result = sum([val for val in mem.values()])
	return result


def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()
		ops = [parse(line) for line in lines]

		ans = solve(ops)

		print(ans)
			
if __name__ == '__main__':
	main() 