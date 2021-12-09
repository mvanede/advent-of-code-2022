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


if __name__ == '__main__':
    unittest.main()
