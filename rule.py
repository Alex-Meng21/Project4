import random
class Rule:

    """A class representing rules"""

    def __init__(self, variable, options):

        self.variable = variable
        self.options = options

    def generate(self):

        """Chooses a random option based on the weight and then generates a sentence fragment"""

        option = random.choices(self.options, [opt.weight for opt in self.options])[0]
        yield from option.generate()
