

from functools import reduce

# CRT taken from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
class CRTSolver:
	
	def chinese_remainder(self, n, a):
		sum = 0
		prod = reduce(lambda a, b: a*b, n)
		for n_i, a_i in zip(n, a):
			p = prod // n_i
			sum += a_i * self.mul_inv(p, n_i) * p
		return sum % prod

	def mul_inv(self, a, b):
		b0 = b
		x0, x1 = 0, 1
		if b == 1: return 1
		while a > 1:
			q = a // b
			a, b = b, a%b
			x0, x1 = x1 - q * x0, x0
		if x1 < 0: x1 += b0
		return x1

def solve(buses):
	solver = CRTSolver()

	mods = []
	result = []

	for bus, offset in buses:
		mods.append(bus)
		result.append(bus - offset)

	return solver.chinese_remainder(mods, result)
	
def main():
	with open("input.txt") as input:
		_ = int(input.readline())
		buses = [(int(bus), idx) for idx, bus in enumerate(input.readline().split(',')) if bus != 'x']

		ans = solve(buses)

		print(ans)
			
if __name__ == '__main__':
	main() 