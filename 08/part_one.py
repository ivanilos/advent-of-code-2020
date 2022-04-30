

def solve(ops):
	nextOp = 0
	ran = set()
	acc = 0

	while nextOp not in ran:
		ran.add(nextOp)
		op, val = ops[nextOp]
		
		
		if op == 'jmp':
			nextOp += int(val)
		else:
			if op == 'acc':
				acc += int(val)

			nextOp += 1
	
	return acc
	
def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()
		ops = [line.split() for line in lines]

		ans = solve(ops)
		print(ans)
			
if __name__ == '__main__':
	main() 