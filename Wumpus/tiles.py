class Tiles(object):
	def __init__(self, coords):
		self.coords = coords
		self.states = set()
		self.prob_wumpus = 0
		self.prob_pit = 0
		self.prob_danger = 0
		self.is_secure = False
	def update_probs(prob_wumpus=0, prob_pit=0):
		self.prob_wumpus += prob_wumpus
		self.prob_pit += prob_pit
		self.prob_danger += (self.prob_wumpus + self.prob_pit)/2
	def __str__(self):
		return str(self.states)