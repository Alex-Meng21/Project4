# project4.py
#
# ICS 33 Winter 2023
# Project 4: Still Looking for Something
from parse_file import process_lines, read_grammar_file
from pathlib import Path
def main() -> None:
    file = input()
    num = int(input())
    variable = input()
    p = Path(file)
    grammar = process_lines(read_grammar_file(p), variable)
    for i in range(num):
        sentence = grammar.generate()
        print(' '.join(sentence))






if __name__ == '__main__':
    main()
