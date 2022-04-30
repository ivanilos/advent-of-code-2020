	

class Ship():
	# N E S W
	deltaPos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3

	DIRECTIONS = 4

	turnDict = {'L' : - 1, 'R' : 1}
	moveDict = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3}
	
	def __init__(self):
		self.x = 0
		self.y = 0
		self.face = Ship.EAST

	def execute(self, command, val):
		if command in ['L', 'R']:
			self.turn(Ship.turnDict[command], val)
		elif command in ['N', 'E', 'S', 'W']:
			self.move(Ship.moveDict[command], val)
		else:
			self.move(self.face, val)

	def turn(self, side, val):
		self.face = ((self.face + side * val // 90) + Ship.DIRECTIONS) % Ship.DIRECTIONS

	def move(self, direction, val):
		self.x += val * Ship.deltaPos[direction][0]
		self.y += val * Ship.deltaPos[direction][1]

	def manhattanFromOrigin(self):
		return abs(self.x) + abs(self.y)

def solve(ops):
	ship = Ship()

	for op in ops:
		ship.execute(*op)

	return ship.manhattanFromOrigin()

	
def main():
	with open("input.txt") as input:
		ops = [(line[0], int(line[1:])) for line in input.read().splitlines()]

		ans = solve(ops)
	
		print(ans)
			
if __name__ == '__main__':
	main() 