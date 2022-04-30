

def solve(ops, ran, nextOp, acc, changedInstruction):
	if nextOp >= len(ops):
		return acc

	while nextOp < len(ops) and (nextOp, changedInstruction) not in ran:
		ran.add((nextOp, changedInstruction))
		op, val = ops[nextOp]
		
		if op == 'jmp':
			if not changedInstruction:
				nextAcc = solve(ops, ran, nextOp + 1, acc, True)
				if nextAcc:
					return nextAcc

			nextOp += int(val)	
		elif op == 'acc':
			acc += int(val)
			nextOp += 1
		elif op == 'nop':
			if not changedInstruction:
				nextAcc = solve(ops, ran, nextOp + int(val), acc, True)
				if nextAcc:
					return nextAcc

			nextOp += 1
	
	return acc if nextOp >= len(ops) else None
	
def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()
		ops = [line.split() for line in lines]

		ran = set()
		ans = solve(ops, ran, 0, 0, False)
		print(ans)
			
if __name__ == '__main__':
	main() 