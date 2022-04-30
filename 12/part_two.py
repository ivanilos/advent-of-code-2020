	

class Ship():
	# N E S W
	deltaPos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
	
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3

	DIRECTIONS = 4

	turnDict = {'L' : (-1, 1), 'R' : (1, -1)}
	moveDict = {'N' : 0, 'E' : 1, 'S' : 2, 'W' : 3}
	
	def __init__(self):
		self.x = 0
		self.y = 0
		self.face = Ship.EAST
		self.waypointX = -1 # X axis increases down
		self.waypointY = 10 # Y axis increases to the right

	def execute(self, command, val):
		if command in ['L', 'R']:
			self.turnWaypoint(Ship.turnDict[command], val)
		elif command in ['N', 'E', 'S', 'W']:
			self.moveWaypoint(Ship.moveDict[command], val)
		else:
			self.move(val)

	def turnWaypoint(self, dirVector, val):
		for _ in range(val // 90):
			self.waypointX, self.waypointY = dirVector[0] * self.waypointY, dirVector[1] * self.waypointX

	def moveWaypoint(self, direction, val):
		self.waypointX += val * Ship.deltaPos[direction][0]
		self.waypointY += val * Ship.deltaPos[direction][1]

	def move(self, val):
		self.x += val * self.waypointX
		self.y += val * self.waypointY

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