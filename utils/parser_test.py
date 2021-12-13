import unittest
from utils import Parser

class ParserTestCase(unittest.TestCase):

    def test_case1_simple_lines_spaces(self):
        f = open("parser_testcases/case1_simple_lines_spaces.txt", "r")
        parsed = Parser.split_by(f.read(), "\n", " ", conv_func=None)

        self.assertEqual(3, len(parsed))
        self.assertEqual('forward', parsed[0][0])
        self.assertEqual('8', parsed[0][1])

        f.close()

    def test_case2_simple_ints(self):
        f = open("parser_testcases/case2_simple_ints.txt", "r")
        parsed = Parser.split_by(f.read(), "\n", conv_func=lambda x:int(x))
        self.assertEqual(5, len(parsed))
        self.assertEqual(150, sum(parsed))
        self.assertEqual(11, parsed[0])

        f.close()

    def test_case3_intlist(self):
        f = open("parser_testcases/case2_simple_ints.txt", "r")
        parsed = Parser.split_by(f.read(), "\n", None, conv_func=lambda x:int(x))
        self.assertEqual(5, len(parsed))
        self.assertEqual(2, len(parsed[0]))
        self.assertEqual(3, len(parsed[4]))

        self.assertEqual(15, sum([sum(x) for x in parsed]))
        f.close()

    def test_case4_int_matrix(self):
        f = open("parser_testcases/case4_test_int_grid.txt", "r")
        parsed = Parser.split_by(f.read(), "\n\n", "\n", None, conv_func=lambda x:int(x))
        self.assertEqual(2, len(parsed))
        self.assertEqual(5, len(parsed[0]))
        self.assertEqual(5, len(parsed[0][0]))
        self.assertEqual(63, sum(parsed[0][0]))

        self.assertEqual(5, len(parsed[1]))
        self.assertEqual(5, len(parsed[1][1]))
        self.assertEqual(69, sum(parsed[1][4]))
        f.close()

    def test_case5_single_line_chars(self):
        parsed = Parser.split_by('abcdef', '', conv_func=None)
        self.assertEqual(6, len(parsed))
        self.assertEqual('a', parsed[0])
        self.assertEqual('f', parsed[5])

    def test_case6_single_line_ints(self):
        parsed = Parser.split_by('123456', '', conv_func=lambda x:int(x))
        self.assertEqual(6, len(parsed))
        self.assertEqual(21, sum(parsed))

    def test_case7_10_to_int(self):
        parsed = Parser.split_by('1x1x10','\n', 'x', conv_func=lambda x: int(x))
        self.assertEqual(1, len(parsed))
        self.assertEqual(3, len(parsed[0]))
        self.assertEqual(12, sum(parsed[0]))

if __name__ == '__main__':
    unittest.main()
