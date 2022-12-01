import unittest
from day_01 import Day01Solution

class AoCTestCase(unittest.TestCase):

    def test_day_01(self):
        s = Day01Solution(use_test_input=False)
        assert s.solve1() == 71471
        assert s.solve2() == 211189


if __name__ == '__main__':
    unittest.main()
