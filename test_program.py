import unittest
from parse_file import test_double_process_lines
from grammar import Grammar
from rule import Rule
from symbol import Terminal, Variable
from option import Option

class MyTestCase(unittest.TestCase):

    def test_parsing_and_adding_them_to_classes(self):
        a = test_double_process_lines("{\nPrintStatement\n1 PRINT [Value]\n}\n{\nValue\n1 Hi\n3 D\n2 D"
                                      ,'PrintStatement')
        self.assertEqual(a.start_var, 'PrintStatement')

        self.assertEqual(a.rules["PrintStatement"].variable, "PrintStatement")

        self.assertEqual(a.rules["PrintStatement"].options[0].weight, 1)

        self.assertEqual(a.rules["PrintStatement"].options[0].symbols[0].symbol, "PRINT")

        self.assertEqual(a.rules["PrintStatement"].options[0].symbols[1].name, "Value")



if __name__ == '__main__':
    unittest.main()
