from rule import Rule
from symbol import Variable, Terminal
from option import Option
from rule import Rule
from grammar import Grammar
def read_grammar_file(file):
    """Generator function that reads the file"""
    with open(file, 'r') as f:
        for line in f:
            yield line

def process_lines(lines, start_variable):
    """Function that processes the lines yielded by read_grammar file
    by checking for options, rules, and symbols and then creating the class objects

    Args:
        lines: the generator function
        start_variable: name of variable obtained from input
    Returns:
        Grammar object with the attributes start_variable and a dictionary containing all the rule objects """
    rules = {}
    current_rule_name = None
    current_rule_options = []

    for line in lines:
        line = line.strip()

        if line.startswith('#') or not line:
            continue

        elif line == "{" and current_rule_name is None:
            current_rule_options = []

        elif line == "}":
            current_rule = Rule(current_rule_name, current_rule_options)
            rules[current_rule_name] = current_rule
            current_rule_name = None
            current_rule_options = []

        elif line[0].isupper():
            current_rule_name = line

        elif line[0].isdigit():
            options = line.split()
            weight = int(options[0])
            symbols = options[1:]
            symbols_list = []

            for sym in symbols:
                if sym.startswith('[') and sym.endswith(']') and (sym[1].isdigit() or sym[1].isalpha()):
                    symbol = Variable(sym[1:-1], rules)
                else:
                    symbol = Terminal(sym)
                symbols_list.append(symbol)

            option = Option(weight, symbols_list)
            current_rule_options.append(option)


    return Grammar(start_variable, rules)


def test_double_process_lines(lines, start_var):
    """Test double for process_lines"""
    rules = {}
    current_rule_name = None
    current_rule_options = []

    for line in lines.splitlines():

        if line.startswith('#') or not line:
            continue

        elif line == "{" and current_rule_name is None:
            current_rule_options = []

        elif line == "}":
            current_rule = Rule(current_rule_name, current_rule_options)
            rules[current_rule_name] = current_rule
            current_rule_name = None
            current_rule_options = []

        elif line[0].isupper():
            current_rule_name = line

        elif line[0].isdigit():
            options = line.split()
            weight = int(options[0])
            symbols = options[1:]
            symbols_list = []

            for sym in symbols:
                if sym.startswith('[') and sym.endswith(']') and (
                        sym[1].isdigit() or sym[1].isalpha()):
                    symbol = Variable(sym[1:-1], rules)
                else:
                    symbol = Terminal(sym)
                symbols_list.append(symbol)

            option = Option(weight, symbols_list)
            current_rule_options.append(option)

    return Grammar(start_var, rules)






