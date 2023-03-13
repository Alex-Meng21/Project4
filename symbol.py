class Terminal:

    def __init__(self, symbol):
        self.symbol = symbol

    def generate_fragment(self):
        yield self.symbol

class Variable:

    def __init__(self, name):
        self.name = name

    def generate_fragment(self):
        pass


