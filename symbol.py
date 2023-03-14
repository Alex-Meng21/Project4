class Terminal:
    """A class representing terminal symbols"""
    def __init__(self, symbol):
        self.symbol = symbol

    def generate(self):
        """Generator method that yields its own value"""
        yield self.symbol

class Variable:
    """A class representing variable symbols"""
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules

    def generate(self):
        """Generator method that looks up the name of the variable in the
        rules dictionary and then asks the rule object to generate a sentence fragment"""

        rule = self.rules[self.name]
        yield from rule.generate()



