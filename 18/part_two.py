

def calcWithoutParenthesis(stack):
	string = ''.join([str(val) for val in stack])

	operandsToMultiply = string.split('*')

	ans = 1
	for operands in operandsToMultiply:
		summands = operands.split('+')
		ans *= sum([int(val) for val in summands])

	return ans

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
			parenthesisExpression = stack[openPositions[-1] + 1 : len(stack)]
			parenthesisVal = ''.join([str(val) for val in parenthesisExpression])

			stack[openPositions[-1]] = calcWithoutParenthesis(parenthesisVal)
			stack = stack[0 : openPositions[-1] + 1]
			openPositions.pop()
		elif ch.isdigit():
			stack.append(int(ch))

	return calcWithoutParenthesis(stack)

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