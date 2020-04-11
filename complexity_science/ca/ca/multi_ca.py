from .rule_manager import RuleManager

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
        for rule in self.rules:
            result = rule.apply(self.cells, self.ca_list)

        self.cells = result
        return self.cells

    def update_ca_list(self):
        for ca in self.ca_list:
            ca.evolve()
