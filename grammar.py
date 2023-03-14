import random
class Grammar:

    def __init__(self, start_var, rules):
        self.start_var = start_var
        self.rules = rules

    def generate(self):

        yield from self.rules[self.start_var].generate()

    def __repr__(self):
        return f"Grammar({self.start_var}, {self.rules})"