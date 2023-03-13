from rule import Rule

def read_grammar_file(file):
    with open(file, 'r') as f:
        for line in f:
            yield line

def process_lines(lines):
    rules = {}
    current_rule_name = None
    for line in lines:
        if line == "{":
            current_rule_options = []
        elif line == "}":
            current_rule = Rule(current_rule_name, current_rule_options)
            rules[current_rule_name] = current_rule
            current_rule_name = None
        elif current_rule_name is None:
            current_rule_name = line
            current_rule_options = []



