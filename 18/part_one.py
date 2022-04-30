

def simplify(stack):
	while len(stack) >= 3:
		if stack[-1] == '(' or stack[-2] == '(':
			break

		right = stack[-1]
		op = stack[-2]
		left = stack[-3]
				
		if op == '+':
			stack[-3] = left + right
		else:
			stack[-3] = left * right

		stack.pop()
		stack.pop()

def calc(expression):
	stack = []
	openPositions = []

	for ch in expression:
		if ch == ' ':
			continue
		elif ch == '+' or ch == '*':
			stack.append(ch)
		elif ch == '(':
			stack.append('(')
			openPositions.append(len(stack) - 1)
		elif ch == ')':
			del stack[openPositions[-1]]
			openPositions.pop()
			simplify(stack)
		elif ch.isdigit():
			stack.append(int(ch))
			simplify(stack)

	return stack[0]

def solve(lines):
	ans = 0

	for line in lines:
		ans += calc(line)

	return ans

def main():
	with open("input.txt") as input:
		lines = input.read().splitlines()

		ans = solve(lines)

		print(ans)
			
if __name__ == '__main__':
	main() 