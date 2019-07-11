from tiles import Tiles
import random

class Board(object):
	def __init__(self):
		self.tiles = []
		self.coords = coords = [(x,y) for y in range(4) for x in range(4)]
		self.is_over = False
		self.create_board()

	def create_board(self):
		self.tiles = [[Tiles((x,y)) for y in range(4)] for x in range(4)]
		self.spawn_objects()

	def spawn_objects(self):
		wumpus_coords = self.spawn_wumpus()
		pit_coords = self.spawn_pit()
		gold_coords = self.spawn_gold()
		self.spawn_breath(wumpus_coords)
		self.spawn_breeze(pit_coords)

	def spawn_wumpus(self):
		wumpus_coords = random.choice(self.coords)
		self.tiles[wumpus_coords[0]][wumpus_coords[1]].states.add("wumpus")
		self.coords.remove(wumpus_coords)
		return wumpus_coords

	def spawn_breath(self, wumpus_coords):
		numrows = len(self.tiles)
		numcols = len(self.tiles[0])
		if wumpus_coords[0] + 1 < numcols:
			self.tiles[wumpus_coords[0] + 1][wumpus_coords[1]].states.add("breath")
		if wumpus_coords[0] - 1 >= 0:
			self.tiles[wumpus_coords[0] - 1][wumpus_coords[1]].states.add("breath")
		if wumpus_coords[1] + 1 < numrows:
			self.tiles[wumpus_coords[0]][wumpus_coords[1] + 1].states.add("breath")
		if wumpus_coords[1] - 1 >= 0:
			self.tiles[wumpus_coords[0]][wumpus_coords[1] - 1].states.add("breath")

	def spawn_breeze(self, pit_coords):
		numrows = len(self.tiles)
		numcols = len(self.tiles[0])
		for pit_coord in pit_coords:
			if pit_coord[0] + 1 < numcols:
				self.tiles[pit_coord[0] + 1][pit_coord[1]].states.add("breeze")
			if pit_coord[0] - 1 >= 0:
				self.tiles[pit_coord[0] - 1][pit_coord[1]].states.add("breeze")
			if pit_coord[1] + 1 < numrows:
				self.tiles[pit_coord[0]][pit_coord[1] + 1].states.add("breeze")
			if pit_coord[1] - 1 >= 0:
				self.tiles[pit_coord[0]][pit_coord[1] - 1].states.add("breeze")

	def spawn_gold(self):
		gold_coords = random.choice(self.coords)
		self.tiles[gold_coords[0]][gold_coords[1]].states.add("gold")
		self.coords.remove(gold_coords)
		return gold_coords

	def spawn_pit(self):
		pit_coords = []
		for i in range(3):
			pit_coords.append(random.choice(self.coords))
			self.tiles[pit_coords[i][0]][pit_coords[i][1]].states.add("pit")
			self.coords.remove(pit_coords[i])
		return pit_coords

	def spawn_player(self):
		return random.choice(self.coords)

	def get_neighbors(self, coords):
		neighbors = []
		numrows = len(self.tiles)
		numcols = len(self.tiles[0])
		if coords[0] + 1 < numcols:
			neighbors.append(self.tiles[coords[0] + 1][coords[1]])
		if coords[0] - 1 >= 0:
			neighbors.append(self.tiles[coords[0] - 1][coords[1]])
		if coords[1] + 1 < numrows:
			neighbors.append(self.tiles[coords[0]][coords[1] + 1])
		if coords[1] - 1 >= 0:
			neighbors.append(self.tiles[coords[0]][coords[1] - 1])
		return neighbors
