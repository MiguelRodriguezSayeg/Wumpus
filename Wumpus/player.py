class Player(object):
	def __init__(self, board):
		self.board = board
		self.current_coords = self.board.spawn_player()
		self.current_tile = None
		self.current_neighbors = []
		self.wumpus_alive = True
		self.score = 0

	def play(self):
		self.current_tile = self.board.tiles[self.current_coords[0]][self.current_coords[1]]
		while not self.board.is_over:
			if "gold" in self.current_tile.states:
				print("Got the gold!")
				self.score += 1000
				self.board.is_over = True
			elif "wumpus" in self.current_tile.states:
				print("Got killed by Wumpus!")
				self.score -= 1000
				self.board.is_over = True
			elif "pit" in self.current_tile.states:
				print("Fell into pit and died!")
				self.score -= 1000
				self.board.is_over = True
			else:
				self.score -= 1
				self.current_neighbors = self.board.get_neighbors(self.current_coords)
				self.current_tile.is_secure = True
				(neighbor.update_probs(prob_pit=1/len(self.current_neighbors)) 
				for neighbor in self.current_neighbors if "breeze" in self.current_tile.states)
				(neighbor.update_probs(prob_wumpus=1/len(self.current_neighbors)) 
				for neighbor in self.current_neighbors if "breath" in self.current_tile.states)
				self.search_wumpus()
				self.current_tile = self.get_best_route()
				self.current_coords = self.current_tile.coords
	def get_best_route(self):
		self.current_neighbors.sort(key=lambda neigh: neigh.prob_danger)
		best_neighbor = self.current_neighbors[0]
		prob_best = []
		i = 0
		for neighbor in self.current_neighbors:
			prob_local = neighbor.prob_danger
			if neighbor.prob_danger < 0.7:
				if not neighbor.is_secure:
					prob_local += 0.1
				else:
					prob_local += 0.2
			prob_best.append(prob_local)
			i+=1
		index = prob_best.index(min(prob_best))
		return self.current_neighbors[index]

	def search_wumpus(self):
		for neighbor in self.current_neighbors:
			if neighbor.prob_wumpus>0.5:
				self.shot(neighbor)
	def shot(self, tile):
		if "wumpus" in tile.states:
			print("Wumpus was shot, you won!")
			self.is_over = True
		else:
			print("You missed the shot.")
