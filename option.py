from symbol import Variable, Terminal
class Option:
    """A class representing options"""
    def __init__(self, weight, symbols):

        self.weight = weight
        self.symbols = symbols

    def generate(self):

        """Iterates through a list of symbol objects and generates the corresponding sentence fragments"""

        for symbol in self.symbols:
            yield from symbol.generate()


