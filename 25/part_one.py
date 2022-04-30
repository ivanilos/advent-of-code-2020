

MOD = 20201227

def transform(subject, loops):
	result = 1
	for _ in range(loops):
		result = (result * subject) % MOD

	return result

def findLoopSize(subject, publicKey):
	num = 1
	loops = 0
	while num != publicKey:
		loops += 1
		num = (num * subject) % MOD

	return loops

def solve(publicKeyA, publicKeyB):
	INITIAL_SUBJECT = 7

	loops = findLoopSize(INITIAL_SUBJECT, publicKeyA)
	result = transform(publicKeyB, loops)

	return result

def main():
	with open("input.txt") as input:
		publicKeyA, publicKeyB = map(int, input.read().splitlines())

		ans = solve(publicKeyA, publicKeyB)

		print(ans)
			
if __name__ == '__main__':
	main() 