class Terminal:

    def __init__(self, symbol):
        self.symbol = symbol

    def generate(self):
        yield self.symbol

class Variable:

    def __init__(self, name, rules):
        self.name = name
        self.rules = rules

    def generate(self):
        rule = self.rules[self.name]
        yield from rule.generate()



