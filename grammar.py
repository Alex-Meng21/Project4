import random
class Grammar:
    """A class representing grammar"""
    def __init__(self, start_var, rules):
        """Attributes:
                start_var: the name of the rule to find
                rules: a dictionary containing all the rule objects
        """
        self.start_var = start_var
        self.rules = rules

    def generate(self):
        """Generator method that searches the rules dictionary for start_var and
        ask the rule to generate a sentence fragment"""

        yield from self.rules[self.start_var].generate()
