import random
class Rule:

    def __init__(self, variable, options):

        self.variable = variable
        self.options = options

    def generate(self):

        option = random.choices(self.options, [opt.weight for opt in self.options])[0]
        yield from option.generate()
