from .rule_manager import RuleManager
import matplotlib.animation as animation

class MultiCA:
    def __init__(self, dim):
        self.size = dim
        self.ca_list = []
        self.rules = []
        self.cells = np.random.random(dim)

    def add_ca(self, ca_object):
        if self.size != ca_object.size:
            print("You are adding a ca object with a different dimension")
        self.ca_list.append(ca_object)

    def reset_ca(self):
        self.ca_list = []

    def add_rule(self, rule_object):
        self.rules.append(rule_object)

    def reset_ca(self):
        self.rules = []

    def evolve(self):
        """
        Evolves the CA according to the rule applied.
        Updates the state of the cell rules can access ca_object in ca_list.

        Returns:
            new_state = new state after applying the rule  
        """
        cell = new_state
        for rule in self.rules:
            result = rule.apply(self.cells, self.ca_list)

        self.cells = result
        return self.cells

    def update_ca_list(self):
        for ca in self.ca_list:
            ca.evolve()

        """ 
        Updates the neighbor according to the new_state
            n1 = left-top neighbor of new_state
            n2 = top neighbor of new_state 
            n3 = right-top neighbor of new_state 
            n4 = left neighbor of new_state 
            n5 = right neighbor of new_state 
            n6 = right-bottom neighbor of new_state
            n7 = bottom neighbor of new_state
            n8 = left-bottom neighbor of new_state
        -------------
        """

    def initialize_random_bin(self, ratio):
        """
        Initializes the ca randomly with a approximated ratio of 1s and 0s 

        Automatically updates neighbors after initialization
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = (ratio > np.random.random(self.size)).astype(int) 
        self.update_neighbors()

    def initialize_random(self):
        """
        Initializes the CA randomly with random values from 0 to 1

        Automatically updates neighbors after initialization
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = np.random.random(self.size)
        self.update_neighbors()

    def initialize_zero(self):
        """
        Initializes the CA with zeros
        Automatically updates neighbors after initialization
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = np.zeros(self.size)
        self.update_neighbors()

    def initialize_index(self, tuple_index, value):
        """
        Initializes an index in the CA with a certain value and 0 for all the rest
        Automatically updates neighbors after initialization
        -------------
        Parameters:
            tuple_index : index on the matrix as tuple
            value : value of the initialization
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = np.zeros(self.size)
        self.cells[index] = value
        self.update_neighbors()
 
    def initialize_random_int(self, min_value, max_value):
        """
        Initializes the ca randomly with integers from min_value to max_value 

        Automatically updates neighbors after initialization
        -------------
        Parameters:
            min_value: lowest possible integer state
            max_value: highest possible integer state

        max_value - min_value = total number of state of the system
        -------------
        Returns:
            None : Updates the cell with initialized values
        """
        self.cells = np.random.randint(min_value, max_value, size=self.size)  
        self.update_neighbors()
        
    def animate(self, num_frames='all', cmap='plasma', savefig=False, writer=animation.writers['ffmpeg']):
        """
        Run animation
        ------------
        Parameters
            Animation parameters
        """
        fig = plt.figure()
        self.im = plt.imshow(self.cells, cmap=cmap, animated=True)

        if num_frames=='all':
            ani = animation.FuncAnimation(fig, self._update_fig, interval=100, blit=True)
            plt.show()
        else:
            ani = animation.FuncAnimation(fig, self._update_fig, interval=100, blit=True, frames=num_frames, repeat=False)
            plt.show()

        if savefig:
            ani.save('Animation.mp4', writer=writer)
	
    def jyp_anim(self, cmap='plasma'):
        fig = plt.figure()
        self.im = plt.imshow(self.cells, cmap=cmap, animated=True)
        anim = animation.FuncAnimation(fig, self._update_fig, interval=100, blit=True)
        return anim

    def _update_fig(self, *args):
        self.im.set_array(self.evolve())
        return self.im,
