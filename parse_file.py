from rule import Rule
from symbol import Variable, Terminal
from option import Option
from rule import Rule
from grammar import Grammar
def read_grammar_file(file):
    with open(file, 'r') as f:
        for line in f:
            yield line

def process_lines(lines, start_variable):
    rules = {}
    current_rule_name = None
    current_rule_options = []
    inside_rule = False
    for line in lines:

        if line.startswith('#'):
            continue

        elif line == "{" and current_rule_name is None:
            current_rule_options = []
            inside_rule = True

        elif line == "}":
            current_rule = Rule(current_rule_name, current_rule_options)
            rules[current_rule_name] = current_rule
            current_rule_name = None
            current_rule_options = []
            inside_rule = False

        elif inside_rule and line[0].upper():
            current_rule_name = line
            current_rule_options = []

        elif inside_rule and line[0].isdigit():
            options = line.split()
            weight = int(options[0])
            symbols = options[1:]
            symbols_list = []

            for sym in symbols:
                if sym.startswith('[') and sym.endswith(']') and (sym[1].isdigit() or sym[1].isalpha()):
                    symbol = Variable(sym[1:-1])
                else:
                    symbol = Terminal(sym)
                symbols_list.append(symbol)

            option = Option(weight, symbols_list)
            current_rule_options.append(option)

    return Grammar(rules, start_variable)







