import unittest
from day_01 import Day01Solution
from day_02 import Day02Solution
from day_03 import Day03Solution

class AoCTestCase(unittest.TestCase):

    def test_day_01(self):
        s = Day01Solution(use_test_input=False)
        assert s.solve1() == 71471
        assert s.solve2() == 211189

    def test_day_02(self):
        s = Day02Solution(use_test_input=False)
        assert s.solve1() == 12645
        assert s.solve2() == 11756

    def test_day_03(self):
        s = Day03Solution(use_test_input=False)
        assert s.solve1() == 7850
        assert s.solve2() == 2581


if __name__ == '__main__':
    unittest.main()
