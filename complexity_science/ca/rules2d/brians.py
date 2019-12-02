import numpy as np

class BriansBrain:
    def apply(self, current, neighbors):
        result = np.zeros_like(current)
        sum_one = np.zeros_like(current)
        for key in neighbors:
            sum_one += (neighbors[key]==1).astype(int)

        current_state = current.copy()
        zero = (current_state ==0)
        two_1 = (sum_one ==2)
        current_state[current_state==2] = 0
        current_state[current_state==1] = 2

        result += current_state
        result += np.logical_and(zero, two_1).astype(int)
        return result
