from symbol import Variable, Terminal
class Option:

    def __init__(self, weight, symbols):

        self.weight = weight
        self.symbols = symbols

    def generate(self):

        for symbol in self.symbols:
            yield from symbol.generate()


