import numpy as np

class ForestFire:
	def __init__(self, **kwargs):
		"""
		Initialize a forest fire rule with default parameters

		states:
		0 = empty
		1 = tree
		2 = burning
		"""
		self.default = {'grow':0.01, 'ignite': 0.01}
		self.update_parameters(**kwargs)

	def update_parameters(self, **kwargs):
		for key, value in kwargs.items():
			self.default[key] = value

		self.grow = self.default['grow']
		self.ignite = self.default['ignite']

	def apply(self, current, neighbors):
		basis = current.copy()
		result = np.zeros_like(current)	
		
		#Grow tree
		empty = (basis==0).astype(int)
		grow_tree = (np.random.random(current.shape) < self.grow).astype(int)
		new_trees = np.logical_and(empty, grow_tree)

		#Ignite tree
		trees = (basis==1).astype(int)
		ignite_tree = (np.random.random(current.shape) < self.ignite).astype(int)
		new_ignite = np.logical_and(trees, ignite_tree)

		#Burn by neighbor
		for key in neighbors:
			sum_burning = (neighbors[key]==2).astype(int)

		#Sum burn by neighbor and new ignited
		burn_by_neighbor = np.logical_and(trees, sum_burning)

		new_fire = np.logical_or(burn_by_neighbor, new_ignite)
		
		burning = (basis==2).astype(int)*-2

		result = basis+new_trees+new_fire+burning

		return result

