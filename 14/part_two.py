
	
MASK_OP = 0
MEM_OP = 1
WORD_SZ = 35

def parse(line):
	left, right = line.split('=')
	left = left.strip()
	right = right.strip()

	if left[0 : 3] == 'mem':
		return (MEM_OP, int(left[4 : len(left) - 1]), int(right))
	else:
		return (MASK_OP, right)

def calc(mask, val):
	bitPos = WORD_SZ

	for bit in mask:
		if bit == '1':
			val |= 1 << bitPos
		elif bit == '0':
			val &= ~(1 << bitPos)

		bitPos -= 1

	return val

def bruteGen(pos, mask, address, result):
	if pos > WORD_SZ:
		result.append(address)
		return
	

	bitPos = WORD_SZ - pos
	if mask[pos] == '0':
		bruteGen(pos + 1, mask, address, result)
	elif mask[pos] == '1':
		bruteGen(pos + 1, mask, address | (1 << bitPos), result)
	else:
		bruteGen(pos + 1, mask, address & ~(1 << bitPos), result)
		bruteGen(pos + 1, mask, address | (1 << bitPos), result)
		

def generate(mask, address):
	result = []

	# uses the fact that 9 is the most quantity of floating (val == 'X') bits in mask
	bruteGen(0, mask, address, result)

	return result

def solve(ops):
	mem = {}
	mask = 0

	for op in ops:
		if op[0] == MASK_OP:
			mask = op[1]
		elif op[0] == MEM_OP:
			for address in generate(mask, op[1]):
				mem[address] = op[2]

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