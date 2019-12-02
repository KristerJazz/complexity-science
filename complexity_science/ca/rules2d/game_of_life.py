import numpy as np

class GameOfLife:
    def apply(self, current, neighbors):
        total_neighbors = np.zeros_like(current)

        for key in neighbors:
            total_neighbors += neighbors[key]

        result = np.zeros_like(current)
        state = current.copy()

        live = (current==1)
        dead = (current==0)
        two = (total_neighbors == 2)
        three = (total_neighbors ==3)

        less_two = (total_neighbors < 2)
        more_three = (total_neighbors >3)
        two_or_three = np.logical_or(two,three)

        result += np.logical_and(live, two_or_three).astype(int)
        result += np.logical_and(dead, three).astype(int)

        state -= np.logical_and(live, less_two).astype(int)
        state -= np.logical_and(live, more_three).astype(int)

        result = np.logical_or(result, state).astype(int)

        return result
